# 🩺 Medical Diagnosis Expert System
# (No external libraries used)

def diagnose():
    print("=== Medical Diagnosis Expert System ===\n")
    print("Answer the following questions with 'yes' or 'no'\n")

    fever = input("Do you have a fever? ").strip().lower()
    cough = input("Do you have a cough? ").strip().lower()
    headache = input("Do you have a headache? ").strip().lower()
    fatigue = input("Are you feeling tired or weak? ").strip().lower()
    sore_throat = input("Do you have a sore throat? ").strip().lower()
    loss_of_smell = input("Have you lost your sense of smell or taste? ").strip().lower()
    runny_nose = input("Do you have a runny or stuffy nose? ").strip().lower()

    print("\nProcessing your symptoms...\n")

    # --- Rule-based diagnosis ---
    if fever == 'yes' and cough == 'yes' and fatigue == 'yes' and loss_of_smell == 'yes':
        print("💡 Diagnosis: You may have COVID-19. Please get tested and isolate.")
    elif fever == 'yes' and cough == 'yes' and fatigue == 'yes':
        print("💡 Diagnosis: You may have the Flu. Rest and stay hydrated.")
    elif runny_nose == 'yes' and sore_throat == 'yes' and fever == 'no':
        print("💡 Diagnosis: You may have a Common Cold. Drink fluids and rest.")
    elif headache == 'yes' and fever == 'yes' and sore_throat == 'yes':
        print("💡 Diagnosis: You may have a Throat Infection. Consult a doctor if it persists.")
    elif fatigue == 'yes' and fever == 'no' and cough == 'no' and headache == 'yes':
        print("💡 Diagnosis: You may be experiencing Fatigue or Mild Dehydration.")
    else:
        print("💡 Diagnosis: Symptoms are unclear. Please consult a doctor for accurate diagnosis.")

    print("\nThank you for using the Medical Diagnosis Expert System.\n")


# --- Run the system ---
if __name__ == "__main__":
    diagnose()
