import joblib
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.feature_extraction.text import TfidfVectorizer


data = pd.read_excel("dataset_genero_musical.xlsx")

print(data.head())

data['musica'] = data['musica'].fillna('') 

X = data['musica']  
y = data['genero']  

vectorizer = TfidfVectorizer()
X_transformed = vectorizer.fit_transform(X)  

X_train, X_test, y_train, y_test = train_test_split(X_transformed, y, test_size=0.2, random_state=42)

model = RandomForestClassifier(n_estimators=100, random_state=42)
model.fit(X_train, y_train)

joblib.dump(model, 'model.joblib')
joblib.dump(vectorizer, 'vectorizer.joblib')  

accuracy = model.score(X_test, y_test)
print(f"Acurácia do modelo: {accuracy:.2f}")
