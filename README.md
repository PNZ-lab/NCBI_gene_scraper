# NCBI_gene_scraper
 Given a list of genes, returns summaries from NCBI

Simply edit the code so that genes_unformatted contains a series of genes with one gene per line.

When executed, this text is formatted to a list containing the gene names, iteratively sent to NCBI, and prints out a summary per gene in a tsv-separated fashion.
This output can be easily formatted to a table by pasting in excel and copying from there. Takes approximately 2s per gene.

### Example input:

    genes_unformatted = '''
    TTC23
    ARHGAP11A-SCG5
    STXBP6
    '''

### Example output:


| Gene Name       | Description                                                                                                                                                                        |
|-----------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| TTC23           | Predicted to be involved in positive regulation of smoothened signaling pathway. Predicted to be located in cilium.|
| ARHGAP11A-SCG5  | This locus represents naturally occurring readthrough transcription between the neighboring ARHGAP11A (Rho GTPase activating protein 11A) and SCG5 (secretogranin V) genes on chromosome 15q13.3. The readthrough transcript encodes a fusion protein that shares sequence identity with both the ARHGAP11A and SCG5 gene products.|
| STXBP6          | Enables cadherin binding activity involved in cell-cell adhesion. Predicted to be involved in negative regulation of exocytosis. Located in adherens junction. |
