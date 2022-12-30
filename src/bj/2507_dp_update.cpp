#include<cstdio>

int DT[500][500];
int D[500];
int S[500];
bool A[500];

int main()
{
    int i,j,k,n,ans=0;
    scanf("%d", &n);
    for(i=0; i<n; i++) scanf("%d %d %d",&D[i],&S[i],&A[i]);
    DT[0][0]=1;

    for(i=0; i<n-1; i++)
    {
        for(j=0; j<n-1; j++)
        {
            if((i==0 && j==0) || (i != j&&A[j]))
            {
                k=i;
                if(k<j) k=j;
                for(k++; k<n; k++)
                {
                if(S[i]>=D[k]-D[i])DT[k][j]=(DT[k][j]+DT[i][j])%1000;
                if(S[k]>=D[k]-D[j])DT[i][k]=(DT[i][k]+DT[i][j])%1000;
                }
            }
        }
    }
    for(i=0; i<n-1; i++) if(S[i]>=D[n-1]-D[i])
        ans=(ans+DT[i][n-1])%1000;
    printf("%d", ans);
    return 0;
}