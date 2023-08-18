class Contract:
    def __init__(self, start_year, end_year, amount):
        self.start_year = start_year
        self.end_year = end_year
        self.amount = amount

class Player:
    def __init__(self, name, position, team):
        self.name = name
        self.position = position
        self.team = team
        self.contracts = []

    def add_contract(self, start_year, end_year, amount):
        contract = Contract(start_year, end_year, amount)
        self.contracts.append(contract)

    def get_total_salary(self):
        total_salary = 0
        for contract in self.contracts:
            total_salary += contract.amount
        return total_salary

# Create players and add contracts
player1 = Player("Patrick Mahomes", "Quarterback", "Kansas City Chiefs")
player1.add_contract(2022, 2026, 45000000)
player1.add_contract(2027, 2030, 50000000)

player2 = Player("Aaron Donald", "Defensive Tackle", "Los Angeles Rams")
player2.add_contract(2021, 2025, 40000000)
player2.add_contract(2026, 2029, 45000000)

# Display player information
print(f"{player1.name} ({player1.position}) - {player1.team}")
print("Contracts:")
for contract in player1.contracts:
    print(f"  {contract.start_year}-{contract.end_year}: ${contract.amount:,}")
print(f"Total Salary: ${player1.get_total_salary():,}\n")

print(f"{player2.name} ({player2.position}) - {player2.team}")
print("Contracts:")
for contract in player2.contracts:
    print(f"  {contract.start_year}-{contract.end_year}: ${contract.amount:,}")
print(f"Total Salary: ${player2.get_total_salary():,}")
