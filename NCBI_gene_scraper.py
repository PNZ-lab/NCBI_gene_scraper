Description='''
This script will take as input several gene names. It then queries NCBI and returns a summary of gene function per gene.
'''

#Email is used for the query in case NCBI needs to contact us
email = 'kasperthorhauge.christensen@ugent.be'

#Just dump genes here with one gene per line.
#They will be formatted to a list as input in the line below
genes_unformatted = '''
LRSAM1
EBF3
OPRL1
TTC23
ARHGAP11A-SCG5
STXBP6
CENPJ
TNFRSF19
SPART
ZNF721
ZBTB7B
SAXO2
ARPP21
CMSS1
SUN1
POLR3C
ASAP2
PRDM8
CDC20B
ST7
CCDC82
ATXN7L3
EOLA2-DT
LRRFIP2
GARS1-DT
NAMPT
SS18
RBBP7
LINC02950
TAF2
PUF60
nan
CFAP157
C9orf43
PDE3B
NCAM1
nan
CASC15
TCN2
CTSH
ALS2CL
SPEF1
GRM4
KANK1
AKR1C2
CNPY1
LINC00662
FKBP10
ZNF566
BAIAP2
HISLA
'''

genes = [gene.strip() for gene in genes_unformatted.split('\n') if gene.strip() and gene.strip().lower() != 'nan']


from Bio import Entrez

# Function to fetch gene summary for Homo sapiens using NCBI's Entrez API
def fetch_gene_summary(gene_name):
    # Set the email to be compliant with NCBI's guidelines
    Entrez.email = email  # Replace with your email address
    
    # Search for the gene in the NCBI Gene database, specifying Homo sapiens
    search_handle = Entrez.esearch(db="gene", term=f"{gene_name}[Gene] AND Homo sapiens[orgn]", retmax=1)
    search_results = Entrez.read(search_handle)
    search_handle.close()

    # If no results are found, return None
    if not search_results["IdList"]:
        print(f"No gene found for {gene_name} in Homo sapiens")
        return None

    # Extract the gene ID
    gene_id = search_results["IdList"][0]
    
    # Fetch the gene summary using the gene ID
    summary_handle = Entrez.esummary(db="gene", id=gene_id)
    summary_results = Entrez.read(summary_handle)
    summary_handle.close()

    # Get the gene summary (includes description, source, organism, etc.)
    gene_summary = summary_results['DocumentSummarySet']['DocumentSummary'][0]
    
    # Return the relevant gene summary
    return gene_summary


for gene in genes:
    gene = gene.upper()
    gene_info = fetch_gene_summary(gene)
    if gene_info:
        # Print the full summary text
        print(gene, '\t', gene_info.get("Summary", "No summary available"))
