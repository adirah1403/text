def welcome():
    print("\n--- Welcome to the Hospital Expert System ---\n")
    print("Please answer the following questions with 'yes' or 'no'.")

def get_input(question):
    while True:
        answer = input(question + " (yes/no): ").strip().lower()
        if answer in ['yes', 'no']:
            return answer
        else:
            print("Please answer only with 'yes' or 'no'.")

def diagnose():
    fever = get_input("Do you have a fever?")
    cough = get_input("Do you have a cough?")
    shortness_of_breath = get_input("Are you experiencing shortness of breath?")
    sore_throat = get_input("Do you have a sore throat?")
    headache = get_input("Do you have a headache?")
    fatigue = get_input("Are you feeling unusually tired?")
    stomach_pain = get_input("Do you have stomach pain?")
    diarrhea = get_input("Do you have diarrhea?")
    chest_pain = get_input("Are you feeling chest pain?")
    rash = get_input("Do you have any skin rashes?")

    print("\n--- Diagnosis Result ---\n")

    # Simple rule-based decision tree
    if fever == 'yes' and cough == 'yes' and shortness_of_breath == 'yes':
        print("Possible Condition: COVID-19 or Severe Respiratory Infection.")
        print("Advice: Get a COVID-19 test immediately and consult a doctor.")
    elif fever == 'yes' and sore_throat == 'yes' and headache == 'yes':
        print("Possible Condition: Common Cold or Flu.")
        print("Advice: Rest, stay hydrated, and consult a doctor if symptoms worsen.")
    elif stomach_pain == 'yes' and diarrhea == 'yes' and fever == 'yes':
        print("Possible Condition: Gastroenteritis (Stomach Flu).")
        print("Advice: Maintain hydration. Seek medical help if condition worsens.")
    elif chest_pain == 'yes' and shortness_of_breath == 'yes':
        print("Possible Condition: Possible Heart Problem (Angina or Heart Attack).")
        print("Advice: Seek Emergency Medical Attention Immediately!")
    elif rash == 'yes' and fever == 'yes':
        print("Possible Condition: Measles or Viral Infection.")
        print("Advice: Visit a hospital for proper diagnosis.")
    elif fatigue == 'yes' and headache == 'yes':
        print("Possible Condition: Mild Viral Infection or Stress.")
        print("Advice: Rest and monitor symptoms.")
    else:
        print("Unable to identify condition precisely based on the given symptoms.")
        print("Advice: Please consult a healthcare professional.")

def main():
    welcome()
    diagnose()
    print("\n--- Thank you for using the Hospital Expert System. Stay Safe! ---\n")

if __name__ == "__main__":
    main()
