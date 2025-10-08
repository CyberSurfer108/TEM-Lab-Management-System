const accounts = [
  { name: "Anthony", age: 17 },
  { name: "Sarah", age: 21 },
  { name: "Mike", age: 15 },
  { name: "Jane", age: 30 }
];

function oldEnough(users) { 
    const adultUsers = [];
    for (let i = 0; i < users.length; i++){
        if (users[i].age >= 18) {
            adultUsers.push(users[i])
        }
    }
    return adultUsers;
};
console.log(oldEnough(accounts))