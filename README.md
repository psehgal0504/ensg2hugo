# ensg2hugo
> This repository contains 3 files
- [ensg2hugo.py](ensg2hugo.py) (This file contains a python code to replaces ensembl gene name with HUGO gene name)
- [expres.anal.csv](expres.anal.csv) (This file contains the ensembl gene name)
- [expres.anal.hugo.csv](expres.anal.hugo.csv) (This is the result file which contains HUGO gene name will be created by our python script)
## ensg2hugo.py
> This program that takes a comma-delimited file as an argument and a column number as an input, and prints a file where the Ensembl gene name has become a HUGO name.
- First step is Homo_sapiens.GRCh37.75.gtf from ensembl website. 
```
curl -o Homo_sapiens.GRCh37.75.gtf.gz http://ftp.ensembl.org/pub/release-75/gtf/homo_sapiens/Homo_sapiens.GRCh37.75.gtf.gz
gunzip Homo_sapiens.GRCh37.75.gtf.gz
```
- The program uses a list as a dictionary to look up substitutions.
- The program uses a regular expression.
- The program is installable using git clone, following README, and have license file as well.
- ENSEMBL gene names match up to the “.” in “ENSG00000248546.3”, since the latter is relevant to build. Thus “ENSG00000248546.3”, “ENSG00000248546.31”, and “ENSG00000248546” should yield “ANP32C”. 
- Allows an option “-f[1-9]” where -f2 would pick the 2nd column. In case another file has a different column, it asks for user input for the gene name column. If there is no “-f” then the first column is used.
```
ensg2hugo.py -f2 expres.anal.csv > expres.anal.hugo.csv
```
will turn this file from
```
1. "","gene_id","gene_name","gene_type","logFC","AveExpr","t","P.Value","adj.P.Val"
2. "14541","ENSG00000248546.3","processed_pseudogene",0.449817926522256,0.0739725408539951,3.47895145072996,0.000284302244388779,0.999999999912779
3. "14546","ENSG00000201050.1","snRNA",0.380944080200912,0.169836608364135,2.92569531023051,0.00183380737252742,0.999999999912779
```
into:
```
1. "","gene_id","gene_name","gene_type","logFC","AveExpr","t","P.Value","adj.P.Val"
2. "14541","ANP32C","processed_pseudogene",0.449817926522256,0.0739725408539951
3. "14546","RNU6-668P","snRNA",0.380944080200912,0.169836608364135,2.92569531023051
```
