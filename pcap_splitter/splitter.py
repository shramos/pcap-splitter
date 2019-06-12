# File from pcap-splitter project
# Copyright (C) 2019 Santiago Hernandez Ramos <shramos@protonmail.com>
# For more information about the project: https://github.com/shramos/pcap-splitter

import subprocess


class PcapSplitter:
    """Split a .pcap file into different files."""

    def __init__(self, pcap_path, exefile_path="PcapSplitter"):
        # Checks if the PcapSplitter executable exists in path
        self._check_binary(exefile_path)
        self._exefile_path = exefile_path
        self._pcap_path = pcap_path

    def split_by_size(self, size_bytes, dest_path, pkts_bpf_filter=""):
        """Split files by size in bytes."""
        args = (self._exefile_path, "-f", self._pcap_path, "-o", dest_path,
                "-m", "file-size", "-p", str(size_bytes), "-i", pkts_bpf_filter)
        # Execute the PcapSplitter binary
        return self._execute(args).decode()

    def split_by_count(self, count_pkts, dest_path, pkts_bpf_filter=""):
        """Split files by packet count."""
        args = (self._exefile_path, "-f", self._pcap_path, "-o", dest_path,
                "-m", "packet-count", "-p", str(count_pkts), "-i", pkts_bpf_filter)
        # Execute the PcapSplitter binary
        return self._execute(args).decode()

    def split_by_client_ip(self, dest_path, pkts_bpf_filter=""):
        """split files by client IP, meaning all connections with the same client 
        IP will be in the same file."""
        args = (self._exefile_path, "-f", self._pcap_path, "-o", dest_path,
                "-m", "client-ip", "-i", pkts_bpf_filter)
        # Execute the PcapSplitter binary
        return self._execute(args).decode()

    def split_by_server_ip(self, dest_path, pkts_bpf_filter=""):
        """split files by server IP, meaning all connections with the same server 
        IP will be in the same file."""
        args = (self._exefile_path, "-f", self._pcap_path, "-o", dest_path,
                "-m", "server-ip", "-i", pkts_bpf_filter)
        # Execute the PcapSplitter binary
        return self._execute(args).decode()

    def split_by_server_port(self, dest_path, pkts_bpf_filter=""):
        """split files by IP src and dst (2-tuple), meaning all connections with 
        the same IPs will be in the same file."""
        args = (self._exefile_path, "-f", self._pcap_path, "-o", dest_path,
                "-m", "server-port", "-i", pkts_bpf_filter)
        # Execute the PcapSplitter binary
        return self._execute(args).decode()

    def split_by_ip_src_dst(self, dest_path, pkts_bpf_filter=""):
        """split files by IP src and dst (2-tuple), meaning all connections with 
        the same IPs will be in the same file."""
        args = (self._exefile_path, "-f", self._pcap_path, "-o", dest_path,
                "-m", "ip-src-dst", "-i", pkts_bpf_filter)
        # Execute the PcapSplitter binary
        return self._execute(args).decode()

    def split_by_session(self, dest_path, pkts_bpf_filter=""):
        """split files by connection (5-tuple), meaning all packets of a 
        connection will be in the same file."""
        args = (self._exefile_path, "-f", self._pcap_path, "-o", dest_path,
                "-m", "connection", "-i", pkts_bpf_filter)
        # Execute the PcapSplitter binary
        return self._execute(args).decode()

    def split_by_filter(self, bpf_filter, dest_path, pkts_bpf_filter=""):
        """split file into two files: one that contains all packets matching the 
        given BPF filter (file #0) and one that contains the rest of the packets 
        (file #1)."""
        args = (self._exefile_path, "-f", self._pcap_path, "-o", dest_path,
                "-m", "bpf-filter", "-p", bpf_filter, "-i", pkts_bpf_filter)
        # Execute the PcapSplitter binary
        return self._execute(args).decode()

    def split_by_round_robin(self, n_files, dest_path, pkts_bpf_filter=""):
        """split the file in a round-robin manner - each packet to a different 
        file."""
        args = (self._exefile_path, "-f", self._pcap_path, "-o", dest_path,
                "-m", "round-robin", "-p", str(n_files), "-i", pkts_bpf_filter)
        # Execute the PcapSplitter binary
        return self._execute(args).decode()

    def _execute(self, args):
        popen = subprocess.Popen(args, stdout=subprocess.PIPE)
        popen.wait()
        return popen.stdout.read()

    def _check_binary(self, exefile_path):
        try:
            subprocess.Popen(exefile_path, stdout=subprocess.PIPE)
        except FileNotFoundError:
            print("ERROR: PcapSplitter executable not found in the OS. Please \
            check that PcapPlusPlus is correctly installed and PcapSplitter \
            executable is in the path, or indicate the path of the PcapSplitter \
            executable by using the exefile_path parameter when instantiating \
            the PcapSplitter class.\n")
