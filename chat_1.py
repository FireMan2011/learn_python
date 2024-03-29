# author: Kondratiuk Maksym, kondratiuk.11.maksim@gmail.com

# -----------------------------
# Чат бот на мінімалках
# -----------------------------

from datetime import date

print("Привіт!")
print("Мене звати Максим.")
print("А як тебе звати?")
name = input()
print("Привіт, " + name)
print("Приємно познайомитись!")
print("Скільки тобі років?")

years = int( input() )

print("В якому місяці ти народився (від 1 до 12)?")
month = int(input())
year_now = int(date.today().year)
current_month = int(date.today().month)

if(current_month >= month):
    old_year = year_now - years
else:
    old_year = year_now - years + 1

print ("В якій день ти народився (від 1 до 31)")
day = int(input())

if(day in range(1, 6)):
    printing_day_text = "Супер я чув що люди які народилися в ці дні дуже розумні особистості"
elif(day in range(6, 11)):
    printing_day_text = "Супер я чув що люди які народилися в ці дні дуже добрі особистості"
elif(day in range(11, 16)):
    printing_day_text = "Супер я чув що люди які народилися в ці дні дуже щедрі особистості"
elif(day in range(16, 21)):
    printing_day_text = "Супер я чув що люди які народилися в ці дні дуже амбіціозні особистості"
elif(day in range(21, 26)):
    printing_day_text = "Супер я чув що люди які народилися в ці дні дуже винахідливі особистості"
elif(day in range(26, 31)):
    printing_day_text = "Супер я чув що люди які народилися в ці дні дуже твочрі особистості"
elif(day == 31):
    printing_day_text = "Супер я чув що люди які народилися в ці дні дуже твочрі, розумні, щедрі, амбіціозні, винахідливі особистості"
else:
    printing_day_text = "Ви мабуть з Поєни!!!"


if(years % 2 == 0):
    old_year = str(old_year) + " (вінтажний дворянмн)"
else:
    old_year = str(old_year) + " (молоденжний аристорат)"

MONTH_NAMES = {
    1: "січні",
    2: "лютому",
    3: "березні",
    4: "квітні",
    5: "травні",
    6: "червні",
    7: "липні",
    8: "серпні",
    9: "вересні",
    10: "жовтні",
    11: "листопаді",
    12: "грудні"
}

printing_text = "О май гад, то ти народився аж у " + MONTH_NAMES[month] + " " + str((old_year))

print(printing_text)
print(printing_day_text)
