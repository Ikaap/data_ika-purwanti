-- cek list node yant terhubung
SELECT *
FROM citus_get_active_worker_nodes();

-- menambahkan node
SELECT *
FROM master_add_node('citus_worker_1', 5432);
SELECT *
FROM master_add_node('citus_worker_2', 5432);

-- create table brands
CREATE TABLE brands(
    brand_id SERIAL PRIMARY KEY,
    name VARCHAR NOT NULL,
    created_at TIMESTAMP DEFAULT NOW() NOT NULL,
    updated_at TIMESTAMP DEFAULT NULL
);
-- insert data table brands
INSERT INTO brands (brand_id, name)
SELECT generate_series,
    'Brand' || generate_series
FROM generate_series(1, 1000);
-- lihat data table brands
SELECT *
FROM brands
LIMIT 20;


-- create table motorcycles
CREATE TABLE motorcycles(
    motorcycle_id SERIAL PRIMARY KEY,
    brand_id INT NOT NULL,
    name VARCHAR NOT NULL,
    color VARCHAR NOT NULL,
    year INT NOT NULL,
    created_at TIMESTAMP DEFAULT NOW() NOT NULL,
    updated_at TIMESTAMP DEFAULT NULL
);
-- insert data table motorcycles
INSERT INTO motorcycles(brand_id, name, color, year)
SELECT (random() * 1000)::int + 1 AS brand_id,
    'Motorcycle' || generate_series,
    'Color' || generate_series,
    2016 + (random() * 8)::int AS year
FROM generate_series (1, 1000000);
-- lihat data table motorcycles
SELECT *
FROM motorcycles
LIMIT 20;


-- create table customers
CREATE TABLE customers (
    customer_id SERIAL PRIMARY KEY,
    name VARCHAR NOT NULL,
    number_phone VARCHAR NOT NULL,
    email VARCHAR NOT NULL,
    address TEXT NOT NULL,
    created_at TIMESTAMP DEFAULT NOW() NOT NULL,
    updated_at TIMESTAMP DEFAULT NULL
);
-- insert data table customers
INSERT INTO customers(name, number_phone, email, address)
SELECT 'Customer' || generate_series,
    concat(
        '+62',
        lpad(trunc(random() * 1000000000)::text, 9, '0')
    ),
    'customer' || generate_series '@gmail.com',
    'Address customer' || generate_series
FROM generate_series(1, 1000000);
-- lihat data table customer
SELECT *
FROM customers
LIMIT 20;


-- create table feedbacks
CREATE TABLE feedbacks(
    feedback_id SERIAL PRIMARY KEY,
    customer_id INT NOT NULL,
    rating FLOAT NOT NULL,
    comment TEXT NOT NULL,
    created_at TIMESTAMP DEFAULT NOW() NOT NULL,
    updated_at TIMESTAMP DEFAULT NULL
);
-- insert data feedbacks
INSERT INTO feedbacks(customer_id, rating, comment)
SELECT (random() * 1000000) + 1 AS customer_id,
    random() * 5 AS rating,
    'Comment customer' || (random() * 1000000) + 1 || ' = Feedback' || generate_series
FROM generate_series(1, 1500000);
-- lihat data feedbacks
SELECT *
FROM feedbacks
LIMIT 10;


-- create table transactions
CREATE TABLE transactions(
    transaction_id SERIAL PRIMARY KEY,
    motorcycle_id INT NOT NULL,
    customer_id INT NOT NULL,
    start_date DATE NOT NULL,
    end_date DATE NOT NULL,
    end_date DATE NOT NULL,
    amount INT NOT NULL,
    guarantee VARCHAR NOT NULL,
    payment_method VARCHAR NOT NULL,
    created_at TIMESTAMP DEFAULT NOW() NOT NULL,
    updated_at TIMESTAMP DEFAULT NULL
) -- insert data transactions
INSERT INTO transactions (
        motorcycle_id,
        customer_id,
        start_date,
        end_date,
        amount,
        guarantee,
        payment_method
    )
SELECT (random() * 1000000) + 1 AS motorcycle_id,
    (random() * 1000000) + 1 AS customer_id,
    '2023-0101'::date + (floor(random() * 356) || ' days')::interval AS start_date,
    (
        '2023-0101'::date + (floor(random() * 356) || ' days')::interval
    ) + (floor(random() * 356) || ' days')::interval AS end_date,
    (random() * 1000) AS amount,
    'Guarantee' || (generate_series % 3 + 1),
    'Payment method' || (generate_series % 5 + 1)
FROM generate_series(1, 2000000)
WHERE '2023-01-01'::date + (floor(random() * 356) || ' days')::interval < ('2023-01-01')::date + (floor(random() * 356) || ' days')::interval + (floor(random() * 356) || ' days')::interval;
-- lihat data table transaction
SELECT *
FROM transactions
LIMIT 15;


-- create table profit
CREATE TABLE profit (
    profit_id SERIAL PRIMARY KEY,
    transaction_id INT NOT NULL,
    profit INT NOT NULL,
    monthly_period DATE NOT NULL,
    created_at TIMESTAMP DEFAULT NOW() NOT NULL,
    updated_at TIMESTAMP DEFAULT NULL
);
-- insert data profit
INSERT INTO profit (transaction_id, profit, monthly_period)
SELECT COALESCE(t.transaction_id, -1) AS transaction_id,
    COALESCE(SUM(t.amount)) AS profit,
    gs.month AS monthly_period
FROM generate_series(
        '2023-01-01'::date,
        '2023-12-31'::date,
        '1 month'
    ) gs(month)
    LEFT JOIN transactions t ON ('month', t.start_date) = gs.month
GROUP BY gs.month,
    t.transaction_id;
-- lihat data table profit
SELECT * FROM profit LIMIT 10;


-- replication
SELECT * FROM pg_dist_placement;
SET citus.shard_replication_factor=2;

-- sharding
SET citus.shard_count TO 4;
SELECT create_distributed_table('brands', brand_id);
SELECT * FROM citus_shards;
SELECT create_distributed_table('motorcycles', motorcycle_id);
SELECT create_distributed_table('customers', customer_id);
SELECT create_distributed_table('feedbacks', feedback_id);
SELECT create_distributed_table('transactions', transaction_id);
SELECT create_distributed_table('profit', profit_id);

-- lihat table di masing-masing shard
SELECT * FROM motorcycles_102044 LIMIT 20;
SELECT * FROM motorcycles_102046 LIMIT 20;
SELECT * FROM motorcycles_102045 LIMIT 20;
SELECT * FROM motorcycles_102047 LIMIT 20;

SELECT * FROM customers_102048 LIMIT 20;
SELECT * FROM customers_102049 LIMIT 20;

SELECT * FROM transactions_102056 LIMIT 20;
SELECT * FROM transactions_102059 LIMIT 20;