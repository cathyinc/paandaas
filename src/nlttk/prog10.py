def display10():
    code = '''import numpy as np
import pandas as pd
from sklearn.decomposition import PCA
from sklearn.preprocessing import StandardScaler
import matplotlib.pyplot as plt
data = {
    'Height': [150, 160, 170, 180, 190],
    'Weight': [50, 60, 65, 80, 90],
    'Age': [25, 30, 35, 40, 45]
}
df = pd.DataFrame(data)
scaler = StandardScaler()
scaled_data = scaler.fit_transform(df)
pca = PCA(n_components=2)
principal_components = pca.fit_transform(scaled_data)
pca_df = pd.DataFrame(
    data=principal_components,
    columns=['pc1', 'pc2']
)
print("Principal components:\\n")
print(pca_df)
print("\\nExplained variance ratio:")
print(pca.explained_variance_ratio_)
plt.scatter(pca_df['pc1'], pca_df['pc2'])
plt.xlabel('Principal Component 1')
plt.ylabel('Principal Component 2')
plt.title('PCA Result')
plt.show()'''
    print(code)
