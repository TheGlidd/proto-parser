//Example at http://www.lemoda.net/c/zlib-open-write/
//Compile with gcc zlib_example.c -lz
//http://stackoverflow.com/questions/1632201/error-deflate-and-inflate-with-zlib


#include <stdio.h>
#include <zlib.h>
#include <stdlib.h>
#include <string.h>

#define CHUNK 0x4000 //why not decimal?

#define CALL_ZLIB(x) {        \
    int status;               \
    status = x;               \
    }                         \
    //if (status < 0) {         \ 
    //    fprintf (stderr);     \
    //    exit (EXIT_FAILURE);  \ 
    //    }                     \ 
    //}                         \

#define windowBits 15
#define GZIP_ENCODING 16

static void strm_init (z_stream * strm) {
    strm->zalloc = Z_NULL;
    strm->zfree = Z_NULL;
    strm->opaque = Z_NULL;
    CALL_ZLIB (deflateInit2 (strm, Z_DEFAULT_COMPRESSION, Z_DEFLATED, windowBits | GZIP_ENCODING, 8, Z_DEFAULT_STRATEGY));
}

static const char * message = "Hi ther";

int main (int argc, char  argv[]) {
    unsigned char out[CHUNK];
    z_stream strm;
    strm_init (& strm);
    strm.next_in = (unsigned char *) message;
    strm.avail_in = strlen(message);
    while (strm.avail_out == 0) {
        int have;
        strm.avail_out = CHUNK;
        strm.next_out = out;
        CALL_ZLIB (deflate (& strm, Z_FINISH));
        have = CHUNK - strm.avail_out;
        fwrite(out, sizeof(char), have, stdout);
    }
    deflateEnd (& strm);

    return 0;
}
