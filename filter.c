#include<stdio.h>
#include<string.h>
main()
{
	FILE *fp,*fp2;
	char str[100],s2[100];
	fp=fopen("contactname","r");
	fp2=fopen("filtered","w");
	strcpy(str,"");
	while(!feof(fp))
	{
		fgets(s2,100,fp);
		if(strcmp(str,s2)!=0)
		{	fprintf(fp2,"%s",s2);
			strcpy(str,s2);	}
	}
	fclose(fp);
	fclose(fp2);
}
