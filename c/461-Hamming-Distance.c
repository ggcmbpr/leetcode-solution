int hammingDistance(int x, int y) {
    int z = x^y;
    int rc = 0;
    while(z>0)
    {
        if( z&1 )
        {
            rc++;      
        }
        z>>=1;
    }
    return rc;
}
