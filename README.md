# Pcap-splitter
Pcap-splitter allows you to split a _.pcap_ file into subsets of _.pcap_ files based on sessions, flows, ip addresses, number of bytes, number of network packets...

To perform these actions, Pcap-splitter makes use of the PcapSplitter tool belonging to the suite [PcapPlusPlus](https://github.com/seladb/PcapPlusPlus).

# Installation
### System Requirements
For Pcap-splitter to work, the installation of the suite PcapPlusPlus is required in the system. To carry out the installation, you can follow the set of steps detailed below or make use of the [installation manual](http://seladb.github.io/PcapPlusPlus-Doc/download.html).
```shell
sudo apt-get install libpcap-dev
git clone https://github.com/seladb/PcapPlusPlus.git
./configure-linux.sh
make all
sudo make install
```
You can also install PcapPlusPlus in any other operating system by downloading [the binaries](https://github.com/seladb/PcapPlusPlus/releases/) and adding them to the path.

### Installation of Pcap-splitter
To install Pcap-splitter execute the following code:
```shell
pip install pcap-splitter
```

# User's manual
Once PcapPlusPlus is installed in the operating system, you can start using pcap-splitter as shown below.

* Example 1
```python
>>> from pcap_splitter.splitter import PcapSplitter

>>> ps = PcapSplitter("network_traffic.pcap")
>>> print(ps.split_by_session("dest_pcaps_folder"))
Started...
Finished. Read and written 27290 packets to 250 files
```
* Example 2
```python
>>> from pcap_splitter.splitter import PcapSplitter

>>> ps = PcapSplitter("network_traffic.pcap")
>>> print(ps.split_by_session("dest_pcaps_folder", pkts_bpf_filter="dst port 80"))
Started...
Finished. Read and written 120 packets to 11 files
```
* Example 3
```python
>>> from pcap_splitter.splitter import PcapSplitter

>>> ps = PcapSplitter("network_traffic.pcap")
>>> print(ps.split_by_count(100, "dest_pcaps_folder"))
Started...
Finished. Read and written 27290 packets to 273 files
```
# Relevant methods
**`split_by_size(self, size_bytes, dest_path, pkts_bpf_filter="")`**  
Split files by size in bytes.

**`split_by_count(self, count_pkts, dest_path, pkts_bpf_filter="")`**   
Split files by packet count.  

**`split_by_client_ip(self, dest_path, pkts_bpf_filter="")`**   
Split files by client IP, meaning all connections with the same client IP will be in the same file.  

**`split_by_server_ip(self, dest_path, pkts_bpf_filter="")`**   
split files by server IP, meaning all connections with the same server IP will be in the same file. 

**`split_by_server_port(self, dest_path, pkts_bpf_filter="")`**    
Split files by IP src and dst (2-tuple), meaning all connections with the same IPs will be in the same file.  

**`split_by_ip_src_dst(self, dest_path, pkts_bpf_filter="")`**   
Split files by IP src and dst (2-tuple), meaning all connections with the same IPs will be in the same file.  

**`split_by_session(self, dest_path, pkts_bpf_filter="")`**   
Split files by connection (5-tuple), meaning all packets of a connection will be in the same file.  

**`split_by_filter(self, bpf_filter, dest_path, pkts_bpf_filter="")`**   
Split file into two files: one that contains all packets matching the given BPF filter (file #0) and one that contains the rest of the packets (file #1). 

**`split_by_round_robin(self, n_files, dest_path, pkts_bpf_filter="")`**   
Split the file in a round-robin manner - each packet to a different file.

# Contact
shramos(at)protonmail(dot)com