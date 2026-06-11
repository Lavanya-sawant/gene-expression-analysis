import pandas as pd

#Load the expression data
expr = pd.read_csv("TCGA-BRCA.star_tpm.tsv", sep="\t")

#Load the clinical data
clinical = pd.read_csv("TCGA-BRCA.clinical.tsv", sep="\t")

#Extract the useful columns from the clinical data
clinical = clinical[["sample", "sample_type.samples"]]

#Convert the sample type to a binary label
clinical["label"] = (
    clinical["sample_type.samples"]
    .map({
        "Primary Tumor":1,
        "Solid Tissue Normal":0
    })
)

expr = expr.set_index(expr.columns[0])
expr = expr.T

merged = expr.merge(
    clinical,
    left_index = True,
    right_on = "sample"
)
from sklearn.feature_selection import SelectKBest
selector = SelectKBest(k=500)

