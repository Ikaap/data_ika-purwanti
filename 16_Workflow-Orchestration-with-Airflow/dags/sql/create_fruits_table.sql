CREATE TABLE IF NOT EXISTS fruits(
    id BIGSERIAL PRIMARY KEY,
    name VARCHAR(255) NOT NULL,
    calories FLOAT NOT NULL,
    fat FLOAT NOT NULL,
    sugar FLOAT NOT NULL,
    carbohydrates FLOAT NOT NULL,
    protein FLOAT NOT NULL
);