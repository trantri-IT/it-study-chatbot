


import streamlit as st
import re
import unicodedata

# ==================================================
# 1. CAU HINH UNG DUNG
# ==================================================

st.set_page_config(
    page_title="IT Study ChatBot",
    page_icon="💻",
    layout="wide",
    initial_sidebar_state="expanded"
)

# ==================================================
# 2. GIAO DIEN CYBER TECH
# ==================================================

st.markdown("""
<style>
.stApp {
    background: linear-gradient(
        135deg, #080d1a 0%, #10172b 55%, #11102a 100%
    );
    color: #e6f1ff;
}

header[data-testid="stHeader"] {
    background: transparent;
}

.block-container {
    max-width: 1100px;
    padding-top: 2rem;
    padding-bottom: 3rem;
}

h1 {
    color: #54f5ff !important;
    font-size: 2.5rem !important;
    font-weight: 800 !important;
    text-shadow: 0 0 18px rgba(84, 245, 255, 0.25);
}

h2, h3 {
    color: #a8b8ff !important;
}

p, label, li {
    color: #d6e3f5;
}

[data-testid="stChatInput"] textarea {
    background-color: #111a2e !important;
    color: #ffffff !important;
    -webkit-text-fill-color: #ffffff !important;
    caret-color: #54f5ff !important;
}

[data-testid="stChatInput"] textarea::placeholder {
    color: #c3d0e5 !important;
    -webkit-text-fill-color: #c3d0e5 !important;
    opacity: 1 !important;
}

[data-testid="stChatInput"] > div {
    border: 1px solid #344766 !important;
    border-radius: 14px !important;
}

[data-testid="stChatInput"] > div:focus-within {
    border-color: #54f5ff !important;
    box-shadow: 0 0 12px rgba(84, 245, 255, 0.2);
}

[data-testid="stChatMessage"] {
    background: rgba(20, 31, 54, 0.75);
    border: 1px solid rgba(84, 245, 255, 0.15);
    border-radius: 16px;
    padding: 12px;
    margin-bottom: 12px;
}

.stButton button {
    background: linear-gradient(90deg, #087fdb, #6554e8);
    color: white !important;
    border: none;
    border-radius: 10px;
    font-weight: 600;
}

.stButton button:hover {
    border: 1px solid #54f5ff;
    box-shadow: 0 0 15px rgba(84, 245, 255, 0.35);
}

[data-testid="stSidebar"] {
    background: #0b1222;
    border-right: 1px solid #263854;
}

hr {
    border-color: #263854;
}

footer {
    visibility: hidden;
}
</style>
""", unsafe_allow_html=True)

# ==================================================
# 3. KHO KIEN THUC CNTT
# ==================================================

KNOWLEDGE = [
    {
        "keywords": ["xin chao", "chao ban", "hello", "hi", "chao"],
        "answer": """
👋 **Xin chào! Mình là IT Study ChatBot.**

Mình có thể giúp bạn học và tìm hiểu:

- 💻 Lập trình Python và phát triển phần mềm
- 🌐 HTML, CSS, JavaScript và website
- ☁️ Cloud Computing, Cloud Native và DevOps
- 🤖 AI, Machine Learning và dữ liệu
- 🔐 An ninh mạng và bảo mật
- 🗄️ Cơ sở dữ liệu và mạng máy tính
- 🎓 Các ngành nghề và lộ trình học CNTT

Bạn muốn học chủ đề nào hôm nay?
"""
    },
    {
        "keywords": [
            "tat ca nganh", "cac nganh nghe", "nganh nghe cntt",
            "nganh cong nghe thong tin", "nganh cntt",
            "nghe nghiep cntt", "cac nghe cntt"
        ],
        "answer": """
# 💻 Các ngành nghề trong CNTT

**1. Phát triển phần mềm**
- Software Engineer: thiết kế và phát triển phần mềm.
- Frontend Developer: xây dựng giao diện website.
- Backend Developer: xử lý dữ liệu và logic phía máy chủ.
- Full-stack Developer: làm cả frontend và backend.
- Mobile Developer: phát triển ứng dụng di động.
- Game Developer: phát triển trò chơi.

**2. Dữ liệu và AI**
- Data Analyst: phân tích dữ liệu.
- Data Engineer: xây dựng hệ thống dữ liệu.
- Data Scientist: nghiên cứu và mô hình hóa dữ liệu.
- Machine Learning Engineer: phát triển hệ thống học máy.
- AI Engineer: tích hợp AI vào ứng dụng.

**3. An ninh mạng**
- Security Analyst: giám sát và phân tích bảo mật.
- Security Engineer: xây dựng hệ thống bảo mật.
- Penetration Tester: kiểm thử bảo mật có sự cho phép.
- Cloud Security Engineer: bảo vệ hạ tầng đám mây.

**4. Cloud và vận hành**
- Cloud Engineer: quản lý hạ tầng đám mây.
- DevOps Engineer: tự động hóa phát triển và triển khai.
- Site Reliability Engineer: cải thiện độ tin cậy hệ thống.
- Platform Engineer: xây dựng nền tảng cho lập trình viên.
- System Administrator: quản trị hệ thống.

**5. Mạng và thiết bị**
- Network Engineer: thiết kế và quản lý mạng.
- Embedded Engineer: phát triển phần mềm nhúng.
- IoT Engineer: phát triển hệ thống Internet vạn vật.

**6. Kiểm thử và chất lượng**
- QA Engineer: đảm bảo chất lượng sản phẩm.
- Software Tester: kiểm thử phần mềm.
- Automation Tester: tự động hóa kiểm thử.

**7. Các vị trí khác**
- UI/UX Designer: thiết kế giao diện và trải nghiệm.
- Business Analyst (BA): phân tích yêu cầu nghiệp vụ.
- Product Manager: định hướng sản phẩm.
- IT Support: hỗ trợ kỹ thuật.
- Database Administrator: quản trị cơ sở dữ liệu.

Đây là những hướng nghề tiêu biểu. Tên gọi và trách nhiệm có thể khác nhau giữa các công ty.
"""
    },
    {
        "keywords": [
            "python", "hoc python", "ngon ngu python",
            "bien trong python", "print python"
        ],
        "answer": """
# 🐍 Python

Python là ngôn ngữ lập trình có cú pháp tương đối dễ đọc.
Nó được dùng trong phát triển phần mềm, tự động hóa, dữ liệu và AI.

**Ví dụ 1: In ra màn hình**

```python
name = "IT Study ChatBot"
print("Xin chào", name)
```

**Ví dụ 2: Biến và phép tính**

```python
a = 10
b = 5
print(a + b)
```

Kết quả là `15`.

**Ví dụ 3: Điều kiện**

```python
age = 18

if age >= 18:
    print("Du tuoi")
else:
    print("Chua du tuoi")
```

**Kiến thức nên học:** biến, kiểu dữ liệu, điều kiện, vòng lặp,
hàm, danh sách, từ điển, xử lý tệp và lập trình hướng đối tượng.
"""
    },
    {
        "keywords": [
            "hoc lap trinh", "bat dau lap trinh",
            "nguoi moi hoc code", "lo trinh lap trinh",
            "hoc code", "lap trinh la gi"
        ],
        "answer": """
# 🎓 Lộ trình học lập trình cho người mới

**Giai đoạn 1: Nền tảng**
- Hiểu biến, kiểu dữ liệu và toán tử.
- Học câu lệnh điều kiện và vòng lặp.
- Viết các hàm đơn giản.

**Giai đoạn 2: Luyện tư duy**
- Giải bài tập nhỏ.
- Học cách đọc lỗi và sửa lỗi.
- Làm quen với Git và GitHub.

**Giai đoạn 3: Làm dự án**
- Máy tính cộng trừ nhân chia.
- Quản lý danh sách công việc.
- Website cá nhân hoặc chatbot đơn giản.

**Giai đoạn 4: Chọn chuyên môn**
- Web: HTML, CSS, JavaScript và backend.
- AI/dữ liệu: Python, toán và xử lý dữ liệu.
- Cloud/DevOps: Linux, mạng, Git, Docker và cloud.

Mẹo: học một chủ đề, thực hành ngay rồi tự làm dự án nhỏ.
"""
    },
    {
        "keywords": [
            "website", "html", "css", "javascript",
            "frontend", "backend", "full stack", "web development"
        ],
        "answer": """
# 🌐 Phát triển website

Website thường được xây dựng bằng nhiều công nghệ kết hợp.

**HTML** tạo cấu trúc nội dung.

**CSS** tạo kiểu dáng, màu sắc và bố cục.

**JavaScript** thêm tương tác cho trang web.

**Frontend** là phần người dùng nhìn thấy và tương tác.

**Backend** xử lý logic, tài khoản, dữ liệu và yêu cầu từ người dùng.

**Database** lưu trữ dữ liệu của ứng dụng.

Ví dụ một website bán hàng có thể dùng HTML/CSS/JavaScript
cho giao diện, Python cho backend và PostgreSQL cho dữ liệu.

**Lộ trình:** HTML → CSS → JavaScript → Git → dự án nhỏ →
backend → cơ sở dữ liệu → triển khai website.
"""
    },
    {
        "keywords": [
            "co so du lieu", "database", "sql", "mysql",
            "postgresql", "mongodb", "he quan tri co so du lieu"
        ],
        "answer": """
# 🗄️ Cơ sở dữ liệu (Database)

Cơ sở dữ liệu dùng để lưu trữ, tổ chức, tìm kiếm và cập nhật thông tin.

**Một số hệ quản trị phổ biến**
- MySQL: cơ sở dữ liệu quan hệ.
- PostgreSQL: cơ sở dữ liệu quan hệ với nhiều tính năng.
- SQLite: gọn nhẹ, phù hợp nhiều ứng dụng nhỏ.
- MongoDB: cơ sở dữ liệu dạng tài liệu.

**Ví dụ SQL**

```sql
CREATE TABLE students (
    id INTEGER PRIMARY KEY,
    name VARCHAR(100)
);

SELECT * FROM students;
```

`CREATE TABLE` tạo bảng; `SELECT` truy vấn dữ liệu.

Nên học bảng, khóa chính, khóa ngoại, quan hệ, truy vấn,
JOIN, chỉ mục và cách bảo vệ dữ liệu.
"""
    },
    {
        "keywords": [
            "cloud computing", "dien toan dam may",
            "cloud la gi", "aws", "azure", "google cloud"
        ],
        "answer": """
# ☁️ Cloud Computing — Điện toán đám mây

Cloud Computing cho phép sử dụng tài nguyên máy tính qua mạng,
chẳng hạn máy chủ, lưu trữ, cơ sở dữ liệu và dịch vụ phần mềm.

**Ba mô hình dịch vụ**
- IaaS: cung cấp hạ tầng như máy ảo và mạng.
- PaaS: cung cấp nền tảng để xây dựng ứng dụng.
- SaaS: sử dụng phần mềm qua Internet.

**Một số nền tảng:** AWS, Microsoft Azure và Google Cloud.

**Ví dụ:** ứng dụng web có thể chạy trên máy chủ đám mây
và lưu dữ liệu trong cơ sở dữ liệu được quản lý.

**Lợi ích:** dễ mở rộng, linh hoạt và giảm nhu cầu tự quản lý
toàn bộ phần cứng.

**Cần lưu ý:** chi phí, bảo mật, quyền truy cập và sao lưu dữ liệu.
"""
    },
    {
        "keywords": [
            "devops", "cloud native", "docker",
            "kubernetes", "ci cd", "cicd", "platform engineering"
        ],
        "answer": """
# ⚙️ DevOps và Cloud Native

**DevOps** kết hợp cách làm việc giữa phát triển phần mềm
và vận hành hệ thống nhằm cải thiện tốc độ và độ tin cậy khi phát hành.

**Cloud Native** là cách thiết kế và vận hành ứng dụng
để tận dụng hiệu quả môi trường đám mây.

**Công nghệ thường gặp**
- Linux: hệ điều hành và môi trường máy chủ.
- Git: quản lý phiên bản mã nguồn.
- Docker: đóng gói ứng dụng và môi trường chạy.
- Kubernetes: điều phối container.
- CI/CD: tự động hóa kiểm thử và triển khai.
- Terraform: quản lý hạ tầng bằng mã.
- Monitoring: theo dõi tình trạng hệ thống.

**Lộ trình gợi ý:** Linux → mạng máy tính → Git →
Docker → CI/CD → cloud → Kubernetes.

Không cần học tất cả cùng lúc. Hãy bắt đầu với Linux, Git
và một ứng dụng nhỏ trước.
"""
    },
    {
        "keywords": [
            "tri tue nhan tao", "artificial intelligence",
            "machine learning", "deep learning",
            "generative ai", "llm", "mo hinh ngon ngu lon",
            "ai la gi", "chatgpt", "ai agent"
        ],
        "answer": """
# 🤖 AI — Trí tuệ nhân tạo

AI là lĩnh vực phát triển hệ thống có thể thực hiện những nhiệm vụ
như nhận dạng, dự đoán, xử lý ngôn ngữ và hỗ trợ ra quyết định.

**Các khái niệm**
- Machine Learning: hệ thống học quy luật từ dữ liệu.
- Deep Learning: sử dụng mạng nơ-ron nhiều lớp.
- Generative AI: tạo nội dung như văn bản, hình ảnh hoặc âm thanh.
- LLM: mô hình ngôn ngữ lớn, được huấn luyện để xử lý ngôn ngữ.
- AI Agent: hệ thống có thể phối hợp các bước hoặc công cụ để hoàn thành nhiệm vụ.

**Ngôn ngữ thường dùng:** Python.

**Kiến thức nên học:** Python, toán cơ bản, thống kê, dữ liệu,
cách đánh giá mô hình và đạo đức AI.

AI có thể tạo ra câu trả lời sai, vì vậy cần kiểm tra thông tin
quan trọng bằng nguồn đáng tin cậy.
"""
    },
    {
        "keywords": [
            "an ninh mang", "cybersecurity", "bao mat",
            "an toan thong tin", "phishing", "ma doc",
            "bao mat tai khoan"
        ],
        "answer": """
# 🔐 An ninh mạng (Cybersecurity)

An ninh mạng bảo vệ hệ thống, ứng dụng và dữ liệu khỏi
truy cập trái phép, tấn công và sự cố bảo mật.

**Các hướng chuyên môn**
- SOC Analyst: giám sát cảnh báo an ninh.
- Security Engineer: xây dựng hệ thống bảo mật.
- Penetration Tester: kiểm thử trong phạm vi được cho phép.
- Application Security: bảo vệ mã nguồn và ứng dụng.
- Cloud Security: bảo vệ hạ tầng đám mây.
- Incident Response: xử lý sự cố an ninh.

**Cách bảo vệ tài khoản**
1. Dùng mật khẩu mạnh và riêng biệt.
2. Bật xác thực đa yếu tố.
3. Không mở liên kết đáng ngờ.
4. Cập nhật phần mềm.
5. Sao lưu dữ liệu quan trọng.

**Lộ trình học:** mạng máy tính → Linux → kiến thức bảo mật cơ bản
→ phòng lab hợp pháp → chọn chuyên môn.

Chỉ kiểm thử các hệ thống mà bạn sở hữu hoặc được cho phép.
"""
    },
    {
        "keywords": [
            "mang may tinh", "network", "tcp ip",
            "dns", "http", "https", "dia chi ip",
            "router", "switch"
        ],
        "answer": """
# 🌐 Mạng máy tính

Mạng máy tính kết nối các thiết bị để trao đổi dữ liệu
và chia sẻ tài nguyên.

**Khái niệm quan trọng**
- IP: địa chỉ định danh mạng của thiết bị.
- DNS: chuyển tên miền thành địa chỉ IP.
- HTTP/HTTPS: giao thức truyền tải dữ liệu web.
- Router: chuyển tiếp dữ liệu giữa các mạng.
- Switch: kết nối thiết bị trong mạng cục bộ.
- TCP: truyền dữ liệu đáng tin cậy theo kết nối.
- UDP: truyền dữ liệu không yêu cầu thiết lập kết nối như TCP.

**Ví dụ:** khi truy cập một website, trình duyệt có thể dùng DNS
để tìm địa chỉ máy chủ rồi trao đổi dữ liệu qua HTTPS.

Người học Cloud, DevOps và an ninh mạng đều cần kiến thức mạng.
"""
    },
    {
        "keywords": [
            "cong nghe phan mem", "ky su phan mem",
            "software engineering", "phat trien phan mem",
            "vong doi phan mem"
        ],
        "answer": """
# 🧩 Công nghệ phần mềm

Công nghệ phần mềm áp dụng các phương pháp kỹ thuật
để phân tích, thiết kế, xây dựng, kiểm thử và bảo trì phần mềm.

**Các giai đoạn thường gặp**
1. Thu thập và phân tích yêu cầu.
2. Thiết kế hệ thống.
3. Lập trình.
4. Kiểm thử.
5. Triển khai.
6. Bảo trì và cải tiến.

**Kỹ năng quan trọng**
- Tư duy logic và giải quyết vấn đề.
- Lập trình và cấu trúc dữ liệu.
- Git và làm việc nhóm.
- Kiểm thử và gỡ lỗi.
- Thiết kế phần mềm và cơ sở dữ liệu.

Lập trình là một phần quan trọng của công nghệ phần mềm,
nhưng kỹ sư phần mềm còn quan tâm đến thiết kế, chất lượng,
khả năng bảo trì và toàn bộ vòng đời sản phẩm.
"""
    },
    {
        "keywords": [
            "kiem thu phan mem", "software testing",
            "qa engineer", "tester", "automation testing",
            "kiem thu tu dong"
        ],
        "answer": """
# 🧪 Kiểm thử phần mềm

Kiểm thử phần mềm giúp phát hiện lỗi và đánh giá xem
ứng dụng có đáp ứng yêu cầu hay không.

**Một số loại kiểm thử**
- Manual Testing: kiểm thử thủ công.
- Automation Testing: tự động hóa các bước kiểm thử.
- Unit Testing: kiểm thử đơn vị nhỏ của chương trình.
- Integration Testing: kiểm tra các thành phần kết hợp.
- Performance Testing: đánh giá hiệu năng.
- Security Testing: đánh giá vấn đề bảo mật.

**Kỹ năng cần học:** phân tích yêu cầu, viết test case,
ghi nhận lỗi, SQL cơ bản và một công cụ kiểm thử.

Kiểm thử nên được thực hiện xuyên suốt quá trình phát triển,
không chỉ ở bước cuối cùng.
"""
    },
    {
        "keywords": [
            "git", "github", "quan ly phien ban",
            "version control", "commit", "branch"
        ],
        "answer": """
# 🛠️ Git và GitHub

Git là công cụ quản lý lịch sử thay đổi của mã nguồn.
GitHub là nền tảng lưu trữ và cộng tác trên các dự án Git.

**Các lệnh cơ bản**

```bash
git init
git status
git add .
git commit -m "Initial commit"
```

- `git init`: khởi tạo kho Git.
- `git status`: xem trạng thái thay đổi.
- `git add`: chọn nội dung chuẩn bị lưu.
- `git commit`: tạo một mốc lịch sử.

Git giúp theo dõi thay đổi, thử nghiệm tính năng bằng branch
và phối hợp làm việc với người khác.
"""
    },
    {
        "keywords": [
            "linux", "he dieu hanh", "terminal",
            "command line", "dong lenh"
        ],
        "answer": """
# 🐧 Linux và dòng lệnh

Linux là hệ điều hành hoặc nhân hệ điều hành được dùng rộng rãi
trên máy chủ, cloud và môi trường phát triển.

**Một số lệnh cơ bản**

```bash
pwd
ls
cd ten_thu_muc
mkdir du_an
```

- `pwd`: hiển thị thư mục hiện tại.
- `ls`: liệt kê nội dung thư mục.
- `cd`: chuyển thư mục.
- `mkdir`: tạo thư mục.

Hãy thực hành trong thư mục cá nhân hoặc môi trường thử nghiệm.
Linux là nền tảng hữu ích cho Cloud, DevOps và an ninh mạng.
"""
    },
    {
        "keywords": [
            "ui ux", "giao dien nguoi dung",
            "trai nghiem nguoi dung", "user experience",
            "user interface"
        ],
        "answer": """
# 🎨 UI/UX Design

**UI (User Interface)** là giao diện mà người dùng nhìn thấy,
như nút bấm, màu sắc, biểu tượng và bố cục.

**UX (User Experience)** là trải nghiệm tổng thể khi sử dụng sản phẩm,
bao gồm tính dễ hiểu, thuận tiện và khả năng hoàn thành mục tiêu.

**Quy trình thường gặp**
1. Tìm hiểu người dùng.
2. Xác định vấn đề.
3. Phác thảo luồng sử dụng.
4. Thiết kế wireframe và prototype.
5. Kiểm thử với người dùng.
6. Cải tiến dựa trên phản hồi.

UI/UX thường phối hợp với lập trình viên và nhóm sản phẩm.
"""
    },
    {
        "keywords": [
            "hoc cntt", "lo trinh cntt", "nen hoc gi",
            "bat dau hoc cntt", "sinh vien cntt",
            "nam nhat cntt"
        ],
        "answer": """
# 🎓 Lộ trình học CNTT cho người mới

**Bước 1: Nền tảng máy tính**
- Sử dụng hệ điều hành và quản lý tệp.
- Hiểu cơ bản về phần cứng và mạng.

**Bước 2: Lập trình**
- Chọn một ngôn ngữ, chẳng hạn Python.
- Học biến, điều kiện, vòng lặp, hàm và cấu trúc dữ liệu.
- Thực hành bài tập thường xuyên.

**Bước 3: Công cụ**
- Git và GitHub.
- SQL và cơ sở dữ liệu.
- Linux cơ bản.

**Bước 4: Dự án**
- Làm một ứng dụng nhỏ.
- Viết hướng dẫn sử dụng.
- Đưa mã nguồn lên GitHub nếu phù hợp.

**Bước 5: Chọn hướng**
Web, phần mềm, AI/dữ liệu, an ninh mạng hoặc Cloud/DevOps.

Không cần học mọi lĩnh vực cùng lúc. Hãy chọn một hướng để thử
rồi điều chỉnh theo sở thích và tiến bộ của bản thân.
"""
    },
    {
        "keywords": [
            "nganh nay co tuong lai khong",
            "xu huong cntt", "xu huong cong nghe",
            "cong nghe moi", "cntt nam 2026"
        ],
        "answer": """
# 🚀 Xu hướng công nghệ cần tìm hiểu

Một số lĩnh vực đang được quan tâm trong ngành CNTT gồm:

- AI và ứng dụng AI tạo sinh.
- An ninh mạng và bảo vệ dữ liệu.
- Cloud Computing và kiến trúc Cloud Native.
- Tự động hóa quy trình phát triển phần mềm.
- Kỹ thuật dữ liệu và phân tích dữ liệu.
- Nền tảng phát triển phần mềm và độ tin cậy hệ thống.

Xu hướng và nhu cầu tuyển dụng thay đổi theo thời gian,
khu vực và doanh nghiệp. Không có lĩnh vực nào bảo đảm việc làm.

Để lựa chọn, hãy cân nhắc sở thích, kỹ năng, cơ hội thực tập
và yêu cầu tuyển dụng thực tế.
"""
    }
]

# ==================================================
# 4. TIM KIEM KHO KIEN THUC
# ==================================================

def normalize_text(text):
    """Chuyen chu thanh dang khong dau de tim tu khoa."""
    text = text.lower().strip()
    text = unicodedata.normalize("NFD", text)
    text = "".join(
        char for char in text
        if unicodedata.category(char) != "Mn"
    )
    text = text.replace("đ", "d")
    return re.sub(r"\s+", " ", text)


def get_answer(question):
    q = normalize_text(question)

    # Tim chu de co tu khoa phu hop nhat
    best_answer = None
    best_score = 0

    for item in KNOWLEDGE:
        score = 0

        for keyword in item["keywords"]:
            normalized_keyword = normalize_text(keyword)

            # Chi tinh tu khoa khi xuat hien trong cau hoi
            if normalized_keyword in q:
                score += len(normalized_keyword.split())

        if score > best_score:
            best_score = score
            best_answer = item["answer"]

    if best_answer:
        return best_answer

    return """
Mình chưa tìm thấy câu trả lời phù hợp trong kho kiến thức hiện tại. 🤔

Bạn có thể thử hỏi cụ thể hơn, chẳng hạn:

- Python là gì?
- Sự khác nhau giữa frontend và backend?
- Cloud Computing là gì?
- DevOps cần học những gì?
- AI và Machine Learning khác nhau thế nào?
- Làm thế nào để bắt đầu học CNTT?

Mình đang dùng kho kiến thức có sẵn nên chưa thể trả lời mọi câu hỏi
hoặc tự cập nhật thông tin mới trên Internet.
"""


# ==================================================
# 5. THANH BEN
# ==================================================

with st.sidebar:
    st.markdown("## 💻 IT STUDY")
    st.caption("YOUR DIGITAL LEARNING SPACE")
    st.markdown("---")

    st.markdown("### 📚 Chủ đề học tập")
    st.markdown("""
    - 🐍 Python
    - 🌐 Web Development
    - 🗄️ Database
    - 🤖 AI & Data
    - 🔐 Cybersecurity
    - ☁️ Cloud & DevOps
    - 🧩 Software Engineering
    """)

    st.markdown("---")
    st.markdown("### ℹ️ Thông tin")
    st.write("Phiên bản: 1.0")
    st.write("Chế độ: Kho kiến thức có sẵn")
    st.write("API: Không cần")

    if st.button("🗑️ Xóa cuộc trò chuyện", use_container_width=True):
        st.session_state.messages = []
        st.rerun()


# ==================================================
# 6. TIEU DE TRANG CHU
# ==================================================

st.title("⌘ IT STUDY ChatBot")
st.caption("◈ YOUR DIGITAL COMPANION • LEARN. CODE. BUILD.")
st.markdown("---")

st.subheader("Trợ lý học tập ngành Công nghệ thông tin")
st.write(
    "Xin chào! Mình giúp bạn học kiến thức CNTT, "
    "luyện lập trình và khám phá các hướng nghề nghiệp."
)

st.info(
    "💡 Mẹo: Hãy đặt câu hỏi cụ thể như "
    "'Python là gì?' hoặc 'DevOps cần học những gì?'"
)

# ==================================================
# 7. LICH SU TRO CHUYEN
# ==================================================

if "messages" not in st.session_state:
    st.session_state.messages = []

for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])


# ==================================================
# 8. NHAP CAU HOI VA TRA LOI
# ==================================================

question = st.chat_input("⌨️ Nhập câu hỏi CNTT của bạn...")

if question:
    st.session_state.messages.append({
        "role": "user",
        "content": question
    })

    with st.chat_message("user"):
        st.markdown(question)

    answer = get_answer(question)

    st.session_state.messages.append({
        "role": "assistant",
        "content": answer
    })

    with st.chat_message("assistant"):
        st.markdown(answer)

# ==================================================
# 9. CHAN TRANG
# ==================================================

st.markdown("---")
st.caption(
    "💻 IT STUDY ChatBot | Công cụ học tập CNTT "
    "| Nội dung tham khảo, hãy kiểm tra thông tin quan trọng."
)
