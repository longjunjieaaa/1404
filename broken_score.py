 def main():
    score = float(input("Enter score: "))
    print(search_result(score))
def search_result(score):
    if score < 0 or score > 100:
        print("Invalid score")
    elif score >= 90:
        print("Excellent")
    elif score >= 50:
        print("Passable")
    else:
        print("Bad")
main()