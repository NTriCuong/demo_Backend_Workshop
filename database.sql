

CREATE TABLE IF NOT EXISTS todos (
    id INT AUTO_INCREMENT PRIMARY KEY,
    title VARCHAR(255) NOT NULL,
    description TEXT,
    is_completed BOOLEAN DEFAULT FALSE,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP
);

INSERT INTO todos (title, description, is_completed)
VALUES
('Học Django REST', 'Tìm hiểu cách tạo API RESTful trong Django', FALSE),
('Làm bài tập MySQL', 'Tạo cơ sở dữ liệu cho Todo App', TRUE);
