# Black-Scholes Calculator Python

This is an interactive Black-Scholes calculator implemented in Python. It allows users to perform various option pricing calculations, including call and put prices, probabilities of ending in the money, and implied volatilities. Users can input the required parameters and receive immediate results for their option pricing calculations.

## Features

- Interactive console-based user interface
- Calculation of different types of Black-Scholes metrics:
  - Call Option Price
  - Put Option Price
  - Probability Call Option in the Money
  - Probability Put Option in the Money
  - Call Option Implied Volatility
  - Put Option Implied Volatility
- Easy-to-follow prompts and detailed explanations for each calculation
- Modular code structure for better organization and maintenance

## How It Works

1. **Main Menu**: The user is presented with a menu of different Black-Scholes formulas to choose from.
2. **User Input**: After selecting a formula, the user is prompted to enter the necessary parameters.
3. **Calculation**: The program performs the calculation based on the user's input and displays the result.
4. **Repeat or Exit**: The user is asked if they want to perform another calculation or exit the program.

## Project Structure

- `black_scholes.py`: Contains all the calculation methods for the Black-Scholes formulas.
- `menu.py`: Handles the user interactions, displays the menu, and processes the user's choices.
- `main.py`: The entry point of the program, manages the main loop for user interaction.

## Usage

To run the program, ensure you have `numpy` and `scipy` installed, then execute the `main.py` file. Follow the prompts to perform your desired option pricing calculations.

### Example Interaction

```
Which Black-Scholes formula would you like to use?
1. Call Option Price
2. Put Option Price
3. Probability Call Option in the Money
4. Probability Put Option in the Money
5. Call Option Implied Volatility
6. Put Option Implied Volatility
user: 1
Recall: S = Stock Price, K = Strike Price, T = Time to Expiration (in years), r = Risk-Free Interest Rate, sigma = Volatility
Enter S, K, T, r, sigma separated by spaces:
user: 44 45 0.167 0.06 0.2
Call Option Price: 2.9518170207100383
The price of a call option is 2.9518170207100383 for stock price 44, strike price 45, time to expiration 0.167 years, risk-free rate 0.06, and volatility 0.2.
Do you want to perform another calculation? (yes/no)
user: no
```

## Formulas

### Call Option Price (C)

$$
C(S_t, t) = \Phi(d_1) S_t - \Phi(d_2) K e^{-rT}
$$
- \( S_t \) = Stock Price
- \( K \) = Strike Price
- \( T \) = Time till expiration (in years)
- \( r \) = Risk-Free Interest Rate
- \( sigma \) = Volatility (standard deviation)
- \( Phi \) = Cumulative Density Function of the standard normal distribution

### Put Option Price (P)

$$
P(S_t, t) = \Phi(-d_2) K e^{-rT} - \Phi(-d_1) S_t
$$
- \( S_t \) = Stock Price
- \( K \) = Strike Price
- \( T \) = Time till expiration (in years)
- \( r \) = Risk-Free Interest Rate
- \( sigma \) = Volatility (standard deviation)
- \( Phi \) = Cumulative Density Function of the standard normal distribution

### Calculating \( d_1 \) and \( d_2 \)

$$
d_1 = \frac{1}{\sigma \sqrt{T}} \left[ \ln\left( \frac{S_t}{K} \right) + \left( r + \frac{\sigma^2}{2} \right) T \right]
$$

$$
d_2 = d_1 - \sigma \sqrt{T}
$$
- \( ln \) = Natural Logarithm

### Probability Call Option in the Money

$$
\text{Probability} = \Phi(d_2)
$$
- \( Phi \) = Cumulative Density Function of the standard normal distribution

### Probability Put Option in the Money

$$
\text{Probability} = 1 - \Phi(d_2)
$$
- \( Phi \) = Cumulative Density Function of the standard normal distribution

### Implied Volatility for Call Option

The implied volatility is the volatility that is implied by the prices of options currently on the market.

### Call Implied Volatility Function

```python
def call_implied_volatility(price, S, K, T, r):
    """ Calculate implied volatility of a call option up to 2 decimals of precision. """
    sigma = 0.0001
    while sigma < 1:
        d1 = BlackScholes._d1(S, K, T, r, sigma)
        d2 = BlackScholes._d2(S, K, T, r, sigma)
        price_implied = S * norm.cdf(d1) - K * np.exp(-r*T) * norm.cdf(d2)
        if abs(price - price_implied) < 0.0001:
            return sigma
        sigma += 0.0001
    return "Not Found"
```

### Put Implied Volatility Function

```python
def put_implied_volatility(price, S, K, T, r):
    """ Calculate implied volatility of a put option up to 2 decimals of precision. """
    sigma = 0.0001
    while sigma < 1:
        call = BlackScholes.call_price(S, K, T, r, sigma)
        price_implied = K * np.exp(-r*T) - S + call
        if abs(price - price_implied) < 0.0001:
            return sigma
        sigma += 0.0001
    return "Not Found"
```

## Running the Program

Ensure all files (`black_scholes.py`, `menu.py`, and `main.py`) are in the same directory or appropriately referenced in your project structure. Install necessary libraries and then execute the `main.py` file:

```sh
pip install numpy scipy
python main.py
```
