import pytest
from bank_account import BankAccount


def test_new_account_starts_with_zero_balance():
    # כאשר נוצר חשבון חדש, היתרה צריכה להיות 0
    account = BankAccount()

    assert account.get_balance() == 0


def test_deposit_money_once():
    # כאשר אני מפקיד 100 דולר, אני מצפה שהיתרה תהיה 100
    account = BankAccount()

    account.deposit(100)
    assert account.get_balance() == 100


def test_deposit_money_twice():
    # כאשר אני מפקיד 100 ואז 50, אני מצפה שהיתרה תהיה 150
    account = BankAccount()

    account.deposit(100)
    account.deposit(50)
    assert account.get_balance() == 150


def test_withdraw_money():
    # כאשר אני מפקיד 100 ומושך 30, אני מצפה שהיתרה תהיה 70
    account = BankAccount()

    account.deposit(100)
    account.withdraw(30)
    assert account.get_balance() == 70


def test_balance_after_deposit_and_withdraw():
    # כאשר אני מפקיד 200, מושך 50, ואז מפקיד 25, אני מצפה שהיתרה תהיה 175
    account = BankAccount()

    account.deposit(200)
    account.withdraw(50)
    account.deposit(25)
    assert account.get_balance() == 175


def test_is_empty_returns_true_for_new_account():
    # כאשר החשבון חדש, אני מצפה ש-is_empty תחזיר True
    account = BankAccount()

    assert account.is_empty() == True


def test_is_empty_returns_false_after_deposit():
    # כאשר אני מפקיד כסף, אני מצפה ש-is_empty תחזיר False
    account = BankAccount()

    account.deposit(200)
    assert account.is_empty() == False