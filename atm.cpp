#include <iostream>

// # TODO : make this accept only numbers

int main()
{
  std::string name;
  int balance = 1000;

  std::cout << "Please enter your name to begin: ";
  std::cin >> name;
  std::cout << "Hello " << name << ", welcome to C++ bank" << std::endl;
  std::cout << "Your current balance is " << balance << std::endl;

  std::string response;
  std::cout << "To withdraw, type 'withdraw'. If you would like to deposit, type 'deposit'." << std::endl;
  std::cin >> response;
  if (response == "withdraw" || response == "Withdraw")
  {
    int withdrawn;
    std::cout << "How much would you like to withdraw?" << std::endl;
    std::cin >> withdrawn;
    int withTotal = balance - withdrawn;
    std::cout << "Your new balance is " << withTotal << std::endl;
  }
  else if (response == "deposit" || response == "Deposit")
  {
    int deposited;
    std::cout << "How much would you like to deposit?" << std::endl;
    std::cin >> deposited;
    int depTotal = balance + deposited;
    std::cout << "Your balance is " << depTotal << std::endl;
  }
  else
  {
    std::cout << "You did not provide a response! Run the ATM once more and try again.";
  }
}
