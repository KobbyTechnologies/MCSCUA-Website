<<<<<<< HEAD
function getBotResponse(input) {
    //rock paper scissors
    if (input == "rock") {
        return "paper";
    } else if (input == "paper") {
        return "scissors";
    } else if (input == "scissors") {
        return "rock";
    }

    // Simple responses
    if (input == "hello" | "Hello") {
        return "Hello there!";
    } else if (input == "goodbye") {
        return "Talk to you later!";
    }else if (input == "I love Your work!") {
        return "Thank you!";
    } else {
        return "Sorry didn't get that, Try asking something else!";
    }
=======
function getBotResponse(input) {
    //rock paper scissors
    if (input == "rock") {
        return "paper";
    } else if (input == "paper") {
        return "scissors";
    } else if (input == "scissors") {
        return "rock";
    }

    // Simple responses
    if (input == "hello" | "Hello") {
        return "Hello there!";
    } else if (input == "goodbye") {
        return "Talk to you later!";
    }else if (input == "I love Your work!") {
        return "Thank you!";
    } else {
        return "Sorry didn't get that, Try asking something else!";
    }
>>>>>>> 89ce836f4d54b5e65ca84936565d5dc8994143e6
}