


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
    },
    {
        "keywords": ["an ninh mang la gi", "cybersecurity la gi", "gioi thieu an ninh mang", "tong quan an ninh mang", "khai niem an ninh mang"],
        "answer": """
# 🔐 Tổng quan về ngành An ninh mạng

**An ninh mạng (Cybersecurity)** là lĩnh vực bảo vệ máy tính, máy chủ, mạng, ứng dụng và dữ liệu khỏi truy cập trái phép, đánh cắp, phá hoại hoặc gián đoạn hoạt động.

**Ba mục tiêu nền tảng – CIA Triad**
- **Confidentiality (Tính bí mật):** chỉ người có quyền mới được xem dữ liệu.
- **Integrity (Tính toàn vẹn):** dữ liệu không bị thay đổi trái phép.
- **Availability (Tính sẵn sàng):** hệ thống và dữ liệu có thể sử dụng khi cần.

An ninh mạng kết hợp công nghệ, quy trình và con người. Không có một công cụ nào bảo vệ tuyệt đối mọi hệ thống.
"""
    },
    {
        "keywords": ["cia triad", "tinh bao mat tinh toan ven tinh san sang", "confidentiality integrity availability"],
        "answer": """
# 🛡️ CIA Triad

CIA Triad là mô hình gồm ba mục tiêu quan trọng của bảo mật thông tin:

1. **Confidentiality – Tính bí mật:** giới hạn dữ liệu cho đúng người được phép.
2. **Integrity – Tính toàn vẹn:** bảo đảm dữ liệu chính xác và không bị sửa trái phép.
3. **Availability – Tính sẵn sàng:** dịch vụ hoạt động khi người dùng hợp lệ cần.

Ví dụ: hệ thống điểm sinh viên cần giữ kín điểm cá nhân, ngăn sửa điểm trái phép và duy trì khả năng truy cập khi đăng ký học phần.
"""
    },
    {
        "keywords": ["nganh an ninh mang hoc gi", "mon hoc an ninh mang", "chuong trinh hoc an ninh mang", "sinh vien an ninh mang hoc gi"],
        "answer": """
# 🎓 Ngành An ninh mạng học gì?

Chương trình tùy trường, nhưng thường có các nhóm kiến thức:

**Nền tảng CNTT:** lập trình, cấu trúc dữ liệu, hệ điều hành, cơ sở dữ liệu, toán rời rạc.

**Mạng và hệ thống:** TCP/IP, DNS, HTTP/HTTPS, định tuyến, Linux, Windows Server và quản trị hệ thống.

**Bảo mật:** mật mã học, xác thực, phân quyền, bảo mật mạng, bảo mật ứng dụng, quản lý lỗ hổng và đánh giá rủi ro.

**Thực hành chuyên sâu:** giám sát an ninh, điều tra số, ứng phó sự cố, bảo mật đám mây và kiểm thử bảo mật trong môi trường được phép.

Hãy xem đề cương chính thức của trường để biết môn học, số tín chỉ và điều kiện tốt nghiệp chính xác.
"""
    },
    {
        "keywords": ["lo trinh hoc an ninh mang", "bat dau hoc cybersecurity", "tu hoc an ninh mang", "nguoi moi hoc an ninh mang"],
        "answer": """
# 🧭 Lộ trình học An ninh mạng cho người mới

1. **Nền tảng máy tính:** hiểu hệ điều hành, tệp, tiến trình và quyền người dùng.
2. **Mạng máy tính:** học IP, DNS, TCP/UDP, HTTP/HTTPS, router và firewall.
3. **Linux và Windows:** sử dụng dòng lệnh, quản lý tài khoản và đọc nhật ký.
4. **Lập trình cơ bản:** bắt đầu với Python; hiểu thêm Bash hoặc PowerShell khi cần.
5. **Kiến thức bảo mật:** xác thực, phân quyền, mã hóa, sao lưu, lỗ hổng và quản lý bản vá.
6. **Thực hành an toàn:** dùng phòng lab học tập, máy ảo hoặc nền tảng được phép.
7. **Chọn hướng:** SOC, bảo mật ứng dụng, kiểm thử bảo mật, cloud security, điều tra số hoặc GRC.

Không cần học mọi thứ cùng lúc. Hãy học nền tảng rồi thực hành từng chủ đề.
"""
    },
    {
        "keywords": ["nghe nghiep an ninh mang", "ra truong an ninh mang lam gi", "cong viec an ninh mang", "vi tri cybersecurity"],
        "answer": """
# 💼 Nghề nghiệp trong An ninh mạng

- **SOC Analyst:** theo dõi cảnh báo, phân tích nhật ký và nhận diện sự kiện đáng ngờ.
- **Security Analyst:** đánh giá nguy cơ và đề xuất biện pháp bảo vệ.
- **Security Engineer:** triển khai, cấu hình và vận hành giải pháp bảo mật.
- **Penetration Tester:** kiểm thử có sự cho phép, ghi nhận và báo cáo lỗ hổng.
- **Incident Responder:** phối hợp điều tra, khoanh vùng và xử lý sự cố.
- **Digital Forensics Analyst:** thu thập, bảo quản và phân tích bằng chứng số.
- **Application Security Engineer:** giúp đội phát triển xây dựng phần mềm an toàn.
- **Cloud Security Engineer:** bảo vệ danh tính, dữ liệu và hạ tầng cloud.
- **GRC Specialist/Auditor:** quản trị rủi ro, chính sách và tuân thủ.

Tên chức danh và yêu cầu khác nhau giữa doanh nghiệp. Người mới thường bắt đầu ở vị trí thực tập, IT support, vận hành hệ thống hoặc SOC cấp đầu vào tùy năng lực.
"""
    },
    {
        "keywords": ["ky nang an ninh mang", "can gi de hoc an ninh mang", "yeu cau an ninh mang", "pham chat chuyen vien an ninh mang"],
        "answer": """
# 🧠 Kỹ năng cần có

**Kỹ năng kỹ thuật**
- Mạng máy tính và hệ điều hành.
- Lập trình cơ bản, thường có thể bắt đầu với Python.
- Đọc nhật ký, phân tích sự kiện và xử lý lỗi.
- Hiểu xác thực, phân quyền, mã hóa và sao lưu.
- Viết báo cáo rõ ràng và ghi lại bằng chứng.

**Kỹ năng bổ trợ**
- Tư duy logic, kiên nhẫn và chú ý chi tiết.
- Tiếng Anh đọc hiểu tài liệu kỹ thuật.
- Giao tiếp và làm việc nhóm.
- Đạo đức nghề nghiệp, tôn trọng quyền riêng tư và phạm vi được cấp phép.

Không nhất thiết phải là chuyên gia toán học ngay từ đầu; quan trọng là học nền tảng đều đặn và thực hành.
"""
    },
    {
        "keywords": ["phishing la gi", "lua dao qua email", "email lua dao", "tin nhan lua dao", "nhan biet phishing"],
        "answer": """
# 🎣 Phishing – Lừa đảo trực tuyến

Phishing là cách kẻ gian giả mạo tổ chức hoặc người đáng tin để dụ nạn nhân tiết lộ mật khẩu, mã xác thực, thông tin cá nhân hoặc chuyển tiền.

**Dấu hiệu cảnh báo**
- Địa chỉ người gửi hoặc tên miền sai khác bất thường.
- Tin nhắn tạo cảm giác khẩn cấp, đe dọa khóa tài khoản.
- Đường dẫn lạ hoặc yêu cầu đăng nhập lại.
- Tệp đính kèm không mong đợi.
- Yêu cầu cung cấp mật khẩu hoặc mã OTP.

**Cách phòng tránh**
1. Tự mở ứng dụng hoặc nhập địa chỉ website chính thức.
2. Kiểm tra kỹ tên miền và người gửi.
3. Không chia sẻ mật khẩu hay mã xác thực.
4. Bật MFA và báo cáo tin nhắn đáng ngờ.
5. Nếu đã nhập thông tin, đổi mật khẩu từ thiết bị đáng tin và liên hệ đơn vị cung cấp dịch vụ.
"""
    },
    {
        "keywords": ["malware la gi", "phan mem doc hai", "virus may tinh", "trojan la gi", "worm la gi"],
        "answer": """
# 🦠 Malware – Phần mềm độc hại

Malware là phần mềm được tạo ra để thực hiện hành vi gây hại hoặc truy cập trái phép.

Các loại thường gặp:
- **Virus:** có thể gắn vào tệp và lây lan khi tệp được thực thi.
- **Worm:** có khả năng tự lan truyền giữa các hệ thống.
- **Trojan:** giả dạng phần mềm hữu ích để thực hiện hành vi không mong muốn.
- **Ransomware:** mã hóa hoặc khóa dữ liệu để tống tiền.
- **Spyware:** theo dõi hoặc thu thập thông tin trái phép.
- **Rootkit:** tìm cách che giấu sự hiện diện hoặc duy trì quyền truy cập.

**Phòng tránh:** cập nhật phần mềm, dùng công cụ bảo vệ đáng tin cậy, hạn chế quyền quản trị, không mở tệp lạ và sao lưu dữ liệu định kỳ.
"""
    },
    {
        "keywords": ["ransomware la gi", "ma doc tong tien", "phong chong ransomware"],
        "answer": """
# 🔒 Ransomware

Ransomware là loại mã độc có thể mã hóa hoặc khóa dữ liệu và đòi tiền chuộc. Trả tiền không bảo đảm dữ liệu sẽ được khôi phục.

**Biện pháp giảm rủi ro**
- Sao lưu theo lịch và giữ bản sao tách biệt.
- Cập nhật hệ điều hành và phần mềm.
- Dùng MFA, hạn chế quyền truy cập và phân đoạn mạng.
- Đào tạo nhận diện email lừa đảo.
- Có kế hoạch ứng phó và kiểm tra khả năng khôi phục.

Nếu nghi ngờ thiết bị bị nhiễm, hãy báo bộ phận IT hoặc người phụ trách, làm theo quy trình ứng phó và tránh tự ý xóa bằng chứng.
"""
    },
    {
        "keywords": ["ddos la gi", "dos la gi", "tan cong tu choi dich vu"],
        "answer": """
# 🌐 DoS và DDoS

**DoS (Denial of Service)** là hành vi làm dịch vụ không thể đáp ứng người dùng hợp lệ. **DDoS** thường sử dụng nhiều thiết bị hoặc nguồn lưu lượng cùng lúc.

Hậu quả có thể là website chậm, gián đoạn hoặc không truy cập được.

**Phòng vệ:** dùng dịch vụ chống DDoS phù hợp, giới hạn lưu lượng, giám sát chỉ số, thiết kế khả năng mở rộng và phối hợp với nhà cung cấp mạng. Chỉ nghiên cứu mô phỏng trong môi trường được phép.
"""
    },
    {
        "keywords": ["firewall la gi", "tuong lua la gi", "cach hoat dong firewall"],
        "answer": """
# 🧱 Firewall – Tường lửa

Firewall kiểm soát lưu lượng mạng dựa trên các quy tắc đã cấu hình. Tùy loại, nó có thể lọc theo địa chỉ IP, cổng, giao thức, ứng dụng hoặc ngữ cảnh kết nối.

**Một số nguyên tắc tốt**
- Chỉ mở những cổng và dịch vụ cần thiết.
- Chặn mặc định những lưu lượng không được cho phép khi phù hợp.
- Ghi nhật ký và thường xuyên rà soát quy tắc.
- Không xem firewall là lớp bảo vệ duy nhất; vẫn cần cập nhật, phân quyền và giám sát.
"""
    },
    {
        "keywords": ["ma hoa la gi", "encryption la gi", "hashing la gi", "bam du lieu la gi", "khac nhau ma hoa va bam"],
        "answer": """
# 🔑 Mã hóa và hàm băm

- **Mã hóa (Encryption):** biến dữ liệu thành dạng khó đọc và có thể giải mã bằng khóa phù hợp.
- **Giải mã (Decryption):** khôi phục dữ liệu từ dạng đã mã hóa khi có khóa cần thiết.
- **Hàm băm (Hashing):** tạo giá trị băm có độ dài xác định; thông thường không dùng để khôi phục trực tiếp dữ liệu gốc.
- **Chữ ký số:** hỗ trợ kiểm tra nguồn gốc và tính toàn vẹn của dữ liệu.
- **Mật mã khóa công khai:** sử dụng một cặp khóa có quan hệ toán học, thường gồm khóa công khai và khóa riêng.

Không nên lưu mật khẩu bằng cách mã hóa có thể giải ngược; hệ thống nên dùng thuật toán băm mật khẩu chuyên dụng kèm salt theo hướng dẫn hiện hành.
"""
    },
    {
        "keywords": ["mfa la gi", "2fa la gi", "xac thuc da yeu to", "otp la gi"],
        "answer": """
# 🔐 MFA và 2FA

**MFA (Multi-Factor Authentication)** yêu cầu ít nhất hai loại yếu tố xác minh khác nhau. **2FA** là trường hợp dùng hai yếu tố.

Các nhóm yếu tố phổ biến:
- Thứ bạn biết: mật khẩu hoặc mã PIN.
- Thứ bạn có: thiết bị hoặc khóa bảo mật.
- Đặc điểm sinh trắc học: ví dụ vân tay.

MFA giúp giảm nguy cơ khi mật khẩu bị lộ. Không chia sẻ mã OTP, không chấp thuận yêu cầu đăng nhập mà bạn không khởi tạo và ưu tiên phương thức chống phishing khi có thể.
"""
    },
    {
        "keywords": ["vpn la gi", "mang rieng ao", "vpn co an toan khong"],
        "answer": """
# 🌍 VPN – Mạng riêng ảo

VPN tạo một kết nối được bảo vệ giữa thiết bị và điểm cuối VPN qua mạng. VPN có thể giúp bảo vệ lưu lượng trên một chặng và hỗ trợ truy cập mạng nội bộ từ xa.

VPN **không** tự động khiến người dùng ẩn danh hoàn toàn, không thay thế antivirus, cập nhật phần mềm hay thói quen an toàn. Hãy chọn nhà cung cấp đáng tin cậy và tuân thủ chính sách của tổ chức.
"""
    },
    {
        "keywords": ["soc analyst la gi", "soc la gi", "security operations center"],
        "answer": """
# 🖥️ SOC Analyst là gì?

SOC (Security Operations Center) là trung tâm hoặc nhóm vận hành giám sát an ninh. SOC Analyst theo dõi cảnh báo từ hệ thống, phân tích nhật ký, xác định mức độ đáng ngờ và chuyển cấp sự cố theo quy trình.

**Kỹ năng thường dùng:** mạng máy tính, Windows/Linux, phân tích log, kiến thức về phishing và malware, SIEM, viết báo cáo và giao tiếp nhóm.

Người mới có thể luyện phân tích các bộ log mẫu và tình huống mô phỏng hợp pháp.
"""
    },
    {
        "keywords": ["kiem thu xam nhap la gi", "penetration testing la gi", "pentest la gi", "pentester la gi"],
        "answer": """
# 🧪 Penetration Testing – Kiểm thử xâm nhập

Penetration testing là hoạt động đánh giá bảo mật có kế hoạch và được cho phép nhằm tìm lỗ hổng, xác định tác động và đề xuất cách khắc phục.

Quy trình khái quát:
1. Xác định phạm vi và có sự cho phép bằng văn bản.
2. Thu thập thông tin trong phạm vi.
3. Kiểm tra các điểm yếu theo quy tắc đã thống nhất.
4. Đánh giá tác động một cách an toàn.
5. Báo cáo phát hiện, bằng chứng và biện pháp khắc phục.
6. Kiểm tra lại sau khi sửa lỗi.

Không kiểm thử website, mạng hoặc tài khoản của người khác khi chưa được cho phép.
"""
    },
    {
        "keywords": ["owasp la gi", "owasp top 10", "lo hong web", "bao mat ung dung web"],
        "answer": """
# 🌐 Bảo mật ứng dụng web và OWASP

Bảo mật ứng dụng web tập trung ngăn lỗi trong thiết kế, lập trình, cấu hình và vận hành.

Các nhóm rủi ro thường được học gồm:
- Kiểm soát truy cập không đúng.
- Lỗi mã hóa và bảo vệ dữ liệu.
- Injection.
- Thiết kế thiếu an toàn.
- Cấu hình bảo mật sai.
- Thành phần phần mềm lỗi thời hoặc dễ tổn thương.
- Xác thực và quản lý phiên không an toàn.
- Thiếu ghi log hoặc giám sát phù hợp.

OWASP cung cấp tài liệu giáo dục và danh sách rủi ro phổ biến. Danh sách có thể được cập nhật, vì vậy hãy xem phiên bản chính thức khi nghiên cứu. Thực hành chỉ trên ứng dụng của bạn hoặc lab được cấp phép.
"""
    },
    {
        "keywords": ["lo hong bao mat la gi", "vulnerability la gi", "quan ly lo hong", "patch la gi"],
        "answer": """
# 🩹 Lỗ hổng và quản lý bản vá

**Lỗ hổng (vulnerability)** là điểm yếu có thể bị lợi dụng để ảnh hưởng đến tính bí mật, toàn vẹn hoặc sẵn sàng của hệ thống.

Quản lý lỗ hổng thường gồm:
1. Lập danh mục tài sản.
2. Quét hoặc đánh giá theo phạm vi được phép.
3. Xác minh và ưu tiên theo mức độ nghiêm trọng, khả năng khai thác và tác động.
4. Cập nhật bản vá hoặc áp dụng biện pháp giảm thiểu.
5. Kiểm tra lại và ghi nhận kết quả.

Không phải mọi lỗ hổng đều có cùng mức độ rủi ro; cần xét bối cảnh hệ thống và dữ liệu được bảo vệ.
"""
    },
    {
        "keywords": ["siem la gi", "edr la gi", "ids ips la gi", "cong cu soc"],
        "answer": """
# 🧰 Công cụ bảo mật thường gặp

- **SIEM:** tập trung và phân tích log từ nhiều nguồn, hỗ trợ tương quan sự kiện và cảnh báo.
- **EDR:** giám sát hoạt động trên thiết bị đầu cuối và hỗ trợ điều tra, phản ứng.
- **IDS:** phát hiện hoạt động mạng hoặc hệ thống đáng ngờ.
- **IPS:** ngoài phát hiện, có thể tự động chặn một số lưu lượng theo cấu hình.
- **Firewall:** kiểm soát lưu lượng theo quy tắc.
- **Vulnerability Scanner:** hỗ trợ tìm cấu hình hoặc phần mềm có điểm yếu.

Công cụ chỉ hữu ích khi được cấu hình phù hợp, cập nhật, giám sát và có người xử lý cảnh báo.
"""
    },
    {
        "keywords": ["cloud security la gi", "bao mat cloud", "bao mat dien toan dam may"],
        "answer": """
# ☁️ Cloud Security – Bảo mật đám mây

Cloud Security bảo vệ dữ liệu, danh tính, ứng dụng và hạ tầng trên nền tảng cloud.

**Các nội dung quan trọng**
- Quản lý danh tính và quyền truy cập (IAM).
- Bật MFA cho tài khoản quan trọng.
- Hạn chế quyền theo nguyên tắc tối thiểu.
- Mã hóa dữ liệu và quản lý khóa.
- Bảo vệ cấu hình lưu trữ, mạng và máy chủ.
- Ghi log, giám sát và cảnh báo.
- Sao lưu, khôi phục và quản lý bí mật an toàn.

Nhà cung cấp cloud và khách hàng thường chia sẻ trách nhiệm bảo mật; trách nhiệm cụ thể phụ thuộc dịch vụ đang dùng.
"""
    },
    {
        "keywords": ["bao mat du lieu la gi", "data privacy", "quyen rieng tu du lieu", "bao ve thong tin ca nhan"],
        "answer": """
# 🗃️ Bảo vệ dữ liệu và quyền riêng tư

Bảo vệ dữ liệu gồm việc ngăn truy cập trái phép, hạn chế sử dụng sai mục đích, giữ dữ liệu chính xác và xử lý an toàn trong suốt vòng đời.

Biện pháp cơ bản:
- Chỉ thu thập dữ liệu cần thiết.
- Phân quyền theo công việc.
- Mã hóa khi phù hợp.
- Sao lưu và kiểm tra khả năng khôi phục.
- Quy định thời hạn lưu trữ và xóa an toàn.
- Ghi nhận truy cập và xử lý sự cố.
- Tuân thủ pháp luật và chính sách áp dụng.

Không đăng tải mật khẩu, khóa API, mã OTP hoặc dữ liệu cá nhân lên kho mã nguồn công khai.
"""
    },
    {
        "keywords": ["ung pho su co an ninh mang", "incident response la gi", "xu ly su co bao mat"],
        "answer": """
# 🚨 Ứng phó sự cố an ninh mạng

Quy trình ứng phó sự cố thường bao gồm:
1. **Chuẩn bị:** lập kế hoạch, phân công trách nhiệm và chuẩn bị công cụ.
2. **Phát hiện và phân tích:** xác minh cảnh báo, xác định phạm vi và mức độ ảnh hưởng.
3. **Khoanh vùng:** hạn chế sự lan rộng theo quy trình của tổ chức.
4. **Loại bỏ nguyên nhân:** xử lý điểm xâm nhập hoặc cấu hình sai.
5. **Khôi phục:** đưa dịch vụ trở lại hoạt động an toàn và theo dõi.
6. **Rút kinh nghiệm:** ghi nhận bài học và cải thiện biện pháp phòng vệ.

Khi xảy ra sự cố thật, hãy báo đội IT/bảo mật hoặc đơn vị có trách nhiệm, giữ lại bằng chứng và làm theo quy trình chính thức.
"""
    },
    {
        "keywords": ["dieu tra so la gi", "digital forensics la gi", "phap chung so"],
        "answer": """
# 🔎 Điều tra số (Digital Forensics)

Điều tra số là quá trình thu thập, bảo quản, kiểm tra và diễn giải dữ liệu số để hiểu sự kiện hoặc hỗ trợ điều tra.

Nguyên tắc quan trọng:
- Có thẩm quyền và phạm vi rõ ràng.
- Bảo toàn tính toàn vẹn của bằng chứng.
- Ghi chép thời gian, công cụ và các thao tác.
- Hạn chế thay đổi dữ liệu gốc.
- Bảo vệ quyền riêng tư và chuỗi quản lý bằng chứng.
- Trình bày kết luận dựa trên bằng chứng, nêu rõ giới hạn.

Đây là lĩnh vực cần phương pháp cẩn thận và tuân thủ pháp luật.
"""
    },
    {
        "keywords": ["grc la gi", "quan tri rui ro an ninh mang", "tuan thu bao mat", "security audit la gi"],
        "answer": """
# 📋 GRC – Quản trị, rủi ro và tuân thủ

GRC là nhóm hoạt động kết nối:
- **Governance (Quản trị):** chính sách, vai trò và trách nhiệm.
- **Risk Management (Quản lý rủi ro):** nhận diện, đánh giá và xử lý rủi ro.
- **Compliance (Tuân thủ):** đáp ứng luật, tiêu chuẩn, hợp đồng và chính sách liên quan.

Công việc có thể gồm lập danh mục tài sản, đánh giá rủi ro, kiểm tra kiểm soát, chuẩn bị bằng chứng kiểm toán và theo dõi khắc phục.
"""
    },
    {
        "keywords": ["zero trust la gi", "nguyen tac quyen toi thieu", "least privilege"],
        "answer": """
# 🧩 Zero Trust và quyền tối thiểu

**Zero Trust** là cách tiếp cận không mặc nhiên tin tưởng người dùng hoặc thiết bị chỉ vì chúng ở trong mạng nội bộ. Việc truy cập cần được xác minh theo danh tính, thiết bị, ngữ cảnh và chính sách.

**Least Privilege – Quyền tối thiểu:** mỗi tài khoản chỉ được cấp những quyền cần thiết để hoàn thành công việc.

Hai nguyên tắc này giúp giảm tác động khi tài khoản bị chiếm quyền hoặc thiết bị gặp sự cố.
"""
    },
    {
        "keywords": ["bao mat mang may tinh", "network security la gi", "bao ve mang"],
        "answer": """
# 🌐 Network Security – Bảo mật mạng

Bảo mật mạng là tập hợp biện pháp bảo vệ thiết bị, kết nối và dữ liệu truyền qua mạng.

Nội dung thường gặp:
- Phân đoạn mạng và kiểm soát truy cập.
- Firewall, IDS/IPS và VPN.
- Bảo vệ Wi-Fi và thiết bị mạng.
- Theo dõi lưu lượng và nhật ký.
- Cập nhật firmware, đổi mật khẩu mặc định.
- Hạn chế dịch vụ và cổng không cần thiết.

Nên kết hợp nhiều lớp bảo vệ và kiểm tra cấu hình định kỳ.
"""
    },
    {
        "keywords": ["bao mat he dieu hanh", "linux security", "bao mat windows"],
        "answer": """
# 🐧 Bảo mật hệ điều hành

Các biện pháp nền tảng:
- Cập nhật hệ điều hành và phần mềm.
- Dùng tài khoản thường cho công việc hằng ngày.
- Cấu hình quyền tệp và thư mục phù hợp.
- Tắt dịch vụ không cần thiết.
- Bật tường lửa và công cụ bảo vệ phù hợp.
- Theo dõi nhật ký đăng nhập và sự kiện.
- Sao lưu dữ liệu và kiểm tra khả năng khôi phục.

Linux và Windows có công cụ quản trị khác nhau, nhưng các nguyên tắc phân quyền, cập nhật và giám sát đều quan trọng.
"""
    },
    {
        "keywords": ["luong nganh an ninh mang", "muc luong cybersecurity", "thu nhap an ninh mang"],
        "answer": """
# 💰 Mức lương ngành An ninh mạng

Mức lương phụ thuộc vào vị trí, kinh nghiệm, ngoại ngữ, khu vực, quy mô doanh nghiệp và kỹ năng chuyên môn. Người mới, chuyên viên có kinh nghiệm và vị trí chuyên sâu có thể có mức thu nhập rất khác nhau.

Để đánh giá thị trường hiện tại, hãy so sánh nhiều tin tuyển dụng mới tại Việt Nam, chú ý yêu cầu công việc, mức lương gross/net, ca trực, phúc lợi và cơ hội đào tạo. Chatbot này không có dữ liệu lương trực tiếp cập nhật theo thời gian thực nên không nên xem một con số cố định là mức chuẩn.
"""
    },
    {
        "keywords": ["chung chi an ninh mang", "chung chi cybersecurity", "certification an ninh mang"],
        "answer": """
# 📜 Chứng chỉ An ninh mạng

Chứng chỉ có thể giúp hệ thống hóa kiến thức hoặc chứng minh kỹ năng, nhưng không thay thế hoàn toàn kinh nghiệm thực hành.

Một số chứng chỉ được biết đến trên thị trường gồm:
- **CompTIA Security+:** nền tảng bảo mật tổng quát.
- **Cisco CCNA:** nền tảng mạng, hữu ích với hướng network security.
- **ISC2 Certified in Cybersecurity (CC):** kiến thức nhập môn về an ninh mạng.
- **OSCP:** chứng chỉ thực hành kiểm thử xâm nhập ở mức chuyên sâu hơn.
- **CISSP:** chứng chỉ rộng về bảo mật, thường phù hợp người đã có kinh nghiệm và cần đáp ứng điều kiện của đơn vị cấp.

Hãy kiểm tra điều kiện, nội dung thi, chi phí và phiên bản hiện hành trên website chính thức trước khi đăng ký.
"""
    },
    {
        "keywords": ["an ninh mang khac cong nghe phan mem", "khac nhau an ninh mang va cong nghe phan mem", "cybersecurity vs software engineering"],
        "answer": """
# ⚖️ An ninh mạng khác Công nghệ phần mềm thế nào?

**Công nghệ phần mềm** tập trung phân tích yêu cầu, thiết kế, xây dựng, kiểm thử, triển khai và bảo trì phần mềm.

**An ninh mạng** tập trung bảo vệ hệ thống, mạng, ứng dụng và dữ liệu khỏi rủi ro bảo mật.

Hai lĩnh vực có phần giao nhau:
- Kỹ sư phần mềm cần viết code an toàn và xử lý lỗ hổng.
- Chuyên viên an ninh mạng cần hiểu phần mềm, hệ điều hành và mạng.
- Application Security kết nối trực tiếp hai lĩnh vực.

Nếu thích xây dựng sản phẩm, bạn có thể nghiêng về phần mềm; nếu thích phân tích rủi ro, bảo vệ hệ thống và điều tra sự cố, có thể khám phá an ninh mạng. Cả hai đều cần tư duy logic và học tập liên tục.
"""
    },
    {
        "keywords": ["an ninh mang va cloud devops", "cloud devops lien quan an ninh mang", "devsecops la gi"],
        "answer": """
# ☁️ Mối liên hệ giữa An ninh mạng, Cloud và DevOps

- **Cloud Security:** bảo vệ danh tính, cấu hình, dữ liệu và hạ tầng đám mây.
- **DevOps:** tự động hóa xây dựng, kiểm thử và triển khai phần mềm.
- **DevSecOps:** đưa kiểm soát bảo mật vào toàn bộ quy trình phát triển và vận hành.

Ví dụ, nhóm có thể tự động kiểm tra phụ thuộc phần mềm, quét cấu hình, quản lý bí mật an toàn và giới hạn quyền triển khai.

Người học Cloud/DevOps sẽ có lợi thế khi hiểu mạng, Linux, IAM, logging và nguyên tắc bảo mật; người học an ninh mạng cũng cần hiểu cách hệ thống được phát triển và vận hành.
"""
    },
    {
        "keywords": ["phong chong tan cong mang", "bao ve may tinh", "lam sao de an toan tren mang", "bao ve tai khoan"],
        "answer": """
# ✅ Cách bảo vệ bản thân trên mạng

1. Dùng mật khẩu mạnh, riêng biệt cho từng tài khoản và cân nhắc trình quản lý mật khẩu.
2. Bật xác thực đa yếu tố.
3. Cập nhật hệ điều hành, trình duyệt và ứng dụng.
4. Kiểm tra đường dẫn, người gửi và tệp đính kèm.
5. Sao lưu dữ liệu quan trọng định kỳ.
6. Chỉ cài phần mềm từ nguồn đáng tin cậy.
7. Hạn chế chia sẻ thông tin cá nhân.
8. Khóa thiết bị khi không sử dụng.
9. Kiểm tra quyền truy cập của ứng dụng.
10. Báo cáo sự cố cho đơn vị liên quan thay vì tự ý xử lý nếu không có chuyên môn.
"""
    },
    {
        "keywords": ["dao duc an ninh mang", "hack co hop phap khong", "hack nguoi khac", "kiem thu khong duoc phep"],
        "answer": """
# ⚖️ Đạo đức và pháp luật trong An ninh mạng

Kỹ năng bảo mật phải được sử dụng có trách nhiệm. Chỉ kiểm thử hệ thống mà bạn sở hữu hoặc đã được chủ sở hữu cho phép, trong phạm vi và thời gian đã thống nhất.

Không truy cập tài khoản người khác, đánh cắp dữ liệu, phát tán mã độc, làm gián đoạn dịch vụ hoặc công bố thông tin riêng tư trái phép.

Khi phát hiện lỗ hổng, hãy ghi nhận tối thiểu cần thiết và báo cáo qua kênh chính thức của đơn vị quản lý. Quy định pháp luật có thể thay đổi; hãy tra cứu nguồn chính thức hoặc hỏi người có chuyên môn pháp lý khi cần.
"""
    },
    {
        "keywords": ["tai lieu hoc an ninh mang", "nguon hoc cybersecurity", "hoc cybersecurity o dau"],
        "answer": """
# 📚 Nguồn học An ninh mạng

Bạn có thể bắt đầu từ các nguồn tài liệu chính thức:
- **NIST NICE Framework:** khung mô tả vai trò, nhiệm vụ, kiến thức và kỹ năng nghề nghiệp: https://www.nist.gov/itl/applied-cybersecurity/nice/nice-framework-resource-center
- **NIST CSRC:** tiêu chuẩn và hướng dẫn an toàn thông tin: https://csrc.nist.gov/
- **CISA:** tài liệu nhận thức và hướng dẫn phòng vệ: https://www.cisa.gov/
- **OWASP:** tài liệu bảo mật ứng dụng web: https://owasp.org/
- **Cisco Networking Academy:** tài liệu nhập môn mạng và an ninh mạng: https://www.netacad.com/

Hãy chọn nội dung phù hợp trình độ và kiểm tra phiên bản tài liệu mới nhất trên trang chính thức.
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
                # Tu khoa cu the/nhieu tu duoc uu tien hon tu khoa qua chung.
                score += len(normalized_keyword.split()) * 3 + min(len(normalized_keyword), 30) / 30

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
    st.write("Phiên bản: 2.0 - Cybersecurity Knowledge")
    st.write("Chế độ: Kho kiến thức mở rộng, tra cứu theo từ khóa")
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
