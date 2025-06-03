# CryptoBuddy: Your AI-powered Financial Sidekick! 🌟

# Predefined Crypto Data
crypto_db = {
    "Bitcoin": {
        "price_trend": "rising",
        "market_cap": "high",
        "energy_use": "high",
        "sustainability_score": 0.3  # 3/10
    },
    "Ethereum": {
        "price_trend": "stable",
        "market_cap": "high",
        "energy_use": "medium",
        "sustainability_score": 0.6  # 6/10
    },
    "Cardano": {
        "price_trend": "rising",
        "market_cap": "medium",
        "energy_use": "low",
        "sustainability_score": 0.8  # 8/10
    }
}

# Chatbot Introduction
print("👋 Hey there! I’m CryptoBuddy — your AI-powered financial sidekick! 🌟")
print("Ask me about crypto trends, sustainability, or long-term investment advice!")

# Start Chat Loop
while True:
    user_query = input("\nYou: ").lower().strip()

    if "exit" in user_query or "quit" in user_query:
        print("CryptoBuddy: 🚀 Catch you later! Remember — crypto is risky, always DYOR (Do Your Own Research)! 📈")
        break

    # Check for sustainable coin
    elif "sustainable" in user_query:
        recommend = max(crypto_db, key=lambda x: crypto_db[x]["sustainability_score"])
        print(f"CryptoBuddy: 🌱 I’d recommend {recommend}! It’s eco-friendly and built for the future!")

    # Check for trending up cryptos
    elif "trending" in user_query or "price" in user_query:
        trending_cryptos = [name for name, data in crypto_db.items() if data["price_trend"] == "rising"]
        if trending_cryptos:
            print(f"CryptoBuddy: 📈 These cryptos are on the rise: {', '.join(trending_cryptos)}!")
        else:
            print("CryptoBuddy: 📉 No cryptos are trending up right now.")

    # Long-term growth advice
    elif "long-term" in user_query or "growth" in user_query:
        options = []
        for name, data in crypto_db.items():
            if data["price_trend"] == "rising" and data["sustainability_score"] >= 0.7:
                options.append(name)
        if options:
            print(f"CryptoBuddy: 🚀 For long-term growth, check out: {', '.join(options)}!")
        else:
            print("CryptoBuddy: 🤔 Hmm, none of the cryptos fully meet long-term growth criteria right now.")

    # Most profitable option
    elif "profitable" in user_query or "best investment" in user_query:
        options = []
        for name, data in crypto_db.items():
            if data["price_trend"] == "rising" and data["market_cap"] == "high":
                options.append(name)
        if options:
            print(f"CryptoBuddy: 💰 The most profitable right now: {', '.join(options)}!")
        else:
            print("CryptoBuddy: 📉 No highly profitable options at the moment — keep an eye on the market!")

    else:
        print("CryptoBuddy: 🤖 Sorry, I didn’t get that. You can ask about 'sustainable', 'trending', 'long-term growth', or 'profitable' cryptos!")

