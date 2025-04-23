// app/webapp/script.js

// Инициализация Web App (полезно при сложной логике)
Telegram.WebApp.ready();

// Пример функции для отправки хода боту
function sendMove() {
    let data = { action: "move", from: "tableau1", to: "foundationHearts" };
    Telegram.WebApp.sendData(JSON.stringify(data));
}

// Пример функции для запроса подсказки
function requestHint(type) {
    let data = { action: "hint", hint_type: type };
    Telegram.WebApp.sendData(JSON.stringify(data));
}

// Обработка ответа от бота (если нужна)
Telegram.WebApp.onEvent("data", function(data) {
    // обработка входящих данных
    console.log("Ответ от бота:", data);
});
