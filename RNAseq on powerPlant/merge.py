import pandas as pd
file1 = pd.read_csv('1_ambrosiaB1_CCADVANXX_GTGGCCTT_L008Aligned.sortedByCoord.out_gene.featureCounts.txt', sep="\t", skiprows=1,usecols = ['Geneid','1_ambrosiaB1_CCADVANXX_GTGGCCTT_L008Aligned.sortedByCoord.out.bam'])
file2 = pd.read_csv('2_ambrosiaB2_CCADVANXX_GTTTCGGA_L008Aligned.sortedByCoord.out_gene.featureCounts.txt', sep="\t", skiprows=1,usecols = ['2_ambrosiaB2_CCADVANXX_GTTTCGGA_L008Aligned.sortedByCoord.out.bam'])
file3 = pd.read_csv('3_ambrosiaB3_CCADVANXX_CGTACGTA_L008Aligned.sortedByCoord.out_gene.featureCounts.txt', sep="\t", skiprows=1,usecols = ['3_ambrosiaB3_CCADVANXX_CGTACGTA_L008Aligned.sortedByCoord.out.bam'])
file4 = pd.read_csv('13_ambrosiaG1_B4_CCADVANXX_CAGATCAT_L008Aligned.sortedByCoord.out_gene.featureCounts.txt', sep="\t", skiprows=1,usecols = ['13_ambrosiaG1_B4_CCADVANXX_CAGATCAT_L008Aligned.sortedByCoord.out.bam'])
file5 = pd.read_csv('14_ambrosiaG2_B5_CCADVANXX_ACTTGAAT_L008Aligned.sortedByCoord.out_gene.featureCounts.txt', sep="\t", skiprows=1,usecols = ['14_ambrosiaG2_B5_CCADVANXX_ACTTGAAT_L008Aligned.sortedByCoord.out.bam'])
file6 = pd.read_csv('15_ambrosiaG3_B6_CCADVANXX_GATCAGAT_L008Aligned.sortedByCoord.out_gene.featureCounts.txt', sep="\t", skiprows=1,usecols = ['15_ambrosiaG3_B6_CCADVANXX_GATCAGAT_L008Aligned.sortedByCoord.out.bam'])
res = pd.concat([file1, file2, file3, file4, file5, file6],axis=1, join='outer').sort_index()
res.to_csv('merge_test.txt', index=False, sep=' ')
