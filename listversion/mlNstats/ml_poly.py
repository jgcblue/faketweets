
from sklearn.preprocessing import PolynomialFeatures

# Create a PolynomialFeatures object with degree 2
poly = PolynomialFeatures(degree=2)

# Transform the x data for polynomial regression
X = np.array(ages).reshape(-1, 1)
y = np.array(rates)
X_poly = poly.fit_transform(X)

# Create and fit the model
poly_model = LinearRegression()
poly_model.fit(X_poly, y)

# Make predictions
y_poly_pred = poly_model.predict(X_poly)

# Plot the results
plt.scatter(X, y, color='blue')
plt.plot(X, y_poly_pred, color='red')
plt.title('Polynomial Regression')
plt.xlabel('Age')
plt.ylabel('Learning Rate')
plt.show()

# Calculate mean squared error
mse_poly = mean_squared_error(y, y_poly_pred)
print('Mean Squared Error (Polynomial):', mse_poly)

# Calculate coefficient of determination (R^2 score)
r2_poly = r2_score(y, y_poly_pred)
print('Coefficient of Determination (R^2 Score) (Polynomial):', r2_poly)
