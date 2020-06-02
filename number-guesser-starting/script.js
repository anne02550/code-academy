let humanScore = 0;
let computerScore = 0;
let currentRoundNumber = 1;

// Write your code below:

const generateTarget = () =>  {
    return Math.floor(Math.random() * 9);
};

const compareGuesses = (huGuess, comGuess, targetNum) => {
    let dis1 = getAbsoluteDistance(targetNum, huGuess);
    let dis2 = getAbsoluteDistance(targetNum, comGuess);
    return dis1 <= dis2;
};

const updateScore = (winner) => {
    if (winner === 'human') {
        humanScore++;
    } else {
        computerScore ++;
    }
}

const advanceRound = () => currentRoundNumber++;

const getAbsoluteDistance = (target, guess) => {
    let distance = Math.abs(target - guess);
    return distance;
}