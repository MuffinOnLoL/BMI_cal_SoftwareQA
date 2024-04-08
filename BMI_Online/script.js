function calculateBMI() {
    var height = document.getElementById("height").value;
    var weight = document.getElementById("weight").value;

    // Calculate BMI
    var bmi = (weight * 703) / (height ** 2)
    var category = getBMICategory(bmi);
    function getBMICategory(bmi) {
        if (bmi < 18.5) {
            return "Underweight";
        } else if (bmi >= 18.5 && bmi < 24.9) {
            return "Normal weight";
        } else if (bmi >= 24.9 && bmi < 29.9) {
            return "Overweight";
        } else {
            return "Obese";
        }
    }
    // Display result
    var resultElement = document.getElementById("result");
    resultElement.innerHTML = "Your BMI is: " + bmi.toFixed(2) + ". You are considered: " + category + ".";
}