/*
compile with gcc sniff.c -lpcap

*/

#include <stdio.h>
#include <pcap.h>

int main(int argc, char *argv[]) {

    //char *dev = "eth0";
    char *dev = "wlan0";
    char errbuf[PCAP_ERRBUF_SIZE];
    pcap_t *handle;
    const u_char *packet;
    struct pcap_pkthdr header;
    
    handle = pcap_open_live(dev, BUFSIZ, 1, 1000, errbuf);
    if (handle == NULL ) {
        fprintf(stderr, "Couldn't open device %s: %s\n", dev, errbuf);
        return 2;
    } 
    
    if (pcap_datalink(handle) != DLT_EN10MB) {
        fprintf(stderr, "Device %s doesn't provide Ethernet headers\n", dev);
        return 2;
    }
    
    packet = pcap_next(handle, &header);
    printf("Jacked length %d\n", header.len);
    pcap_close(handle);

    return 0;

}
