# Hướng dẫn build app Ghi chú thành file APK (cài thẳng lên Samsung, dùng offline hoàn toàn)

Làm đúng theo thứ tự. Toàn bộ miễn phí, không cần cài Android Studio trên máy bạn — việc build sẽ chạy tự động trên máy chủ của GitHub.

---

## Bước 1 — Tạo tài khoản GitHub (nếu chưa có)

1. Vào https://github.com/signup, đăng ký miễn phí bằng email.

## Bước 2 — Tạo một "kho chứa code" (repository) mới

1. Sau khi đăng nhập, bấm nút **+** góc trên phải → **New repository**.
2. Đặt tên, ví dụ: `ghi-chu-app`
3. Chọn **Private** (riêng tư, chỉ mình bạn thấy) hoặc Public đều được.
4. Bấm **Create repository**.

## Bước 3 — Tải toàn bộ thư mục này lên GitHub

Cách dễ nhất, không cần dùng lệnh:

1. Trong trang repository vừa tạo, bấm **uploading an existing file** (hoặc "Add file" → "Upload files").
2. Kéo thả **toàn bộ nội dung** thư mục `ghi-chu-android` (đã giải nén) vào — bao gồm cả thư mục `.github` và `www` bên trong (kéo cả thư mục là được, GitHub tự giữ đúng cấu trúc).
3. Bấm **Commit changes** để lưu.

> Lưu ý: thư mục `.github` có dấu chấm ở đầu — trên một số trình quản lý file bạn cần bật "hiện file ẩn" mới thấy nó khi kéo thả. Nếu dùng máy tính, hầu hết trình duyệt kéo-thả vẫn nhận diện được thư mục ẩn này bình thường.

## Bước 4 — Để GitHub tự động build file APK

1. Sau khi tải file lên xong, vào tab **Actions** ở trên cùng repository.
2. Bạn sẽ thấy một quy trình tên "Build Android APK" đang chạy (hoặc bấm vào nó rồi bấm **Run workflow** nếu chưa tự chạy).
3. Đợi khoảng 5-8 phút để build xong (icon tròn xoay chuyển thành dấu tích xanh ✓).

## Bước 5 — Tải file APK về

1. Sau khi thấy dấu tích xanh ✓, bấm vào lần chạy đó.
2. Kéo xuống mục **Artifacts**, bấm vào **ghi-chu-apk** để tải về — đây chính là file `.apk`.
3. Giải nén file zip vừa tải, bên trong có file `app-debug.apk`.

## Bước 6 — Cài file APK lên điện thoại Samsung

1. Chuyển file `app-debug.apk` vào điện thoại (qua cáp USB, tải trực tiếp trên điện thoại nếu bạn làm bước 5 ngay trên điện thoại, hoặc gửi qua Zalo/email cho chính mình).
2. Trên điện thoại, vào **Cài đặt → Bảo mật** (hoặc "Ứng dụng và thông báo" tùy đời máy) → bật **Cho phép cài đặt ứng dụng từ nguồn không xác định** cho trình duyệt/app quản lý file bạn dùng để mở file apk.
3. Mở file `app-debug.apk` bằng trình quản lý file → bấm **Cài đặt**.
4. Xong! App "Ghi chú" giờ có icon riêng trong danh sách app, mở lên chạy hoàn toàn độc lập — không cần mạng, không cần trình duyệt, giống hệt Samsung Notes.

---

## Rất quan trọng — về micro (giọng nói)

Khi chạy trong app Android đóng gói (khác với mở qua trình duyệt), tính năng giọng nói **có thể cần thêm bước cấp quyền micro cho app** lần đầu tiên — điện thoại sẽ tự hỏi "Cho phép Ghi chú truy cập micro?" → bấm **Cho phép**. Nếu không tự hỏi, vào Cài đặt → Ứng dụng → Ghi chú → Quyền → bật Micro thủ công.

## Khi cần cập nhật app (thêm tính năng mới sau này)

Mỗi khi mình sửa file `index.html` để thêm tính năng, bạn chỉ cần:
1. Vào lại repository trên GitHub, mở file `www/index.html`, bấm biểu tượng bút chì để sửa, dán nội dung mới vào, Commit.
2. Quay lại tab Actions, đợi build xong, tải file APK mới, cài đè lên bản cũ (dữ liệu ghi chú cũ vẫn giữ nguyên vì lưu riêng trong bộ nhớ app, không bị mất khi cập nhật).
