import numpy as np
import pandas as pd
from sklearn.preprocessing import MinMaxScaler
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import LSTM, Dense
import matplotlib.pyplot as plt

class TimeSeriesPredictor:
    def __init__(self, window_size=60):
        self.window_size = window_size
        self.scaler = MinMaxScaler()
        self.model = self._build_model()
        self.is_fitted = False

    def _build_model(self):
        """Создание архитектуры LSTM модели"""
        model = Sequential([
            LSTM(50, return_sequences=False, input_shape=(self.window_size, 1)),
            Dense(25, activation='relu'),
            Dense(1)
        ])
        model.compile(optimizer='adam', loss='mean_squared_error')
        return model

    def prepare_data(self, data):
        """
        Создание скользящих окон из данных
        Вход: [t-window_size, ..., t-1]
        Выход: [t]
        """
        X, y = [], []
        for i in range(len(data) - self.window_size):
            X.append(data[i:(i + self.window_size)])
            y.append(data[i + self.window_size])
        return np.array(X), np.array(y)

    def normalize(self, data):
        """Нормализация данных (Min-Max scaling)"""
        return self.scaler.fit_transform(data.reshape(-1, 1)).flatten()

    def denormalize(self, normalized_data):
        """Денормализация данных"""
        return self.scaler.inverse_transform(normalized_data.reshape(-1, 1)).flatten()

    def train(self, data, epochs=50, validation_split=0.1):
        """Обучение модели"""
        # Нормализация данных
        normalized_data = self.normalize(data)
        
        # Подготовка скользящих окон
        X, y = self.prepare_data(normalized_data)
        
        # Изменение формы данных для LSTM (samples, timesteps, features)
        X = X.reshape((X.shape[0], X.shape[1], 1))
        y = y.reshape((y.shape[0], 1))
        
        # Обучение модели
        history = self.model.fit(
            X, y,
            epochs=epochs,
            batch_size=32,
            validation_split=validation_split,
            verbose=1
        )
        
        self.is_fitted = True
        return history

    def predict(self, last_window):
        """Предсказать следующее значение"""
        if not self.is_fitted:
            raise ValueError("Модель не обучена. Сначала вызовите метод train().")
        
        # Нормализуем окно
        normalized_window = self.scaler.transform(last_window.reshape(-1, 1))
        
        # Изменяем форму для модели
        X = normalized_packed_window.reshape((1, self.window_size, 1))
        
        # Делаем предсказание
        predicted = self.model.predict(X, verbose=0)
        
        # Денормализуем результат
        return self.denormalize(predicted)[0]

    def plot_predictions(self, actual_data, predicted_data, title="Прогноз цен акций"):
        """Визуализация предсказаний"""
        plt.figure(figsize=(14, 7))
        plt.plot(actual_data, label='Фактические значения', color='blue')
        plt.plot(predicted_data, label='Предсказанные значения', color='red', linestyle='--')
        plt.title(title)
        plt.xlabel('Временные шаги')
        plt.ylabel('Цена акции')
        plt.legend()
        plt.grid(True)
        plt.show()
