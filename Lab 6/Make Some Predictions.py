# Fit the best model
best_model = KNeighborsClassifier()
best_model.fit(X_train, y_train)

# Make predictions
predictions = best_model.predict(X_validation)

# Evaluate predictions
from sklearn.metrics import classification_report, confusion_matrix

print(confusion_matrix(y_validation, predictions))
print(classification_report(y_validation, predictions))
