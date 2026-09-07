# Tầm nhìn xa của các tòa nhà cao tầng

## Bối cảnh

Dọc con đường ven biển của thành phố có $N$ tòa nhà cao tầng đứng san sát nhau, mỗi tòa cao một số mét nhất định. Hiệp hội du lịch muốn chọn những tòa nhà có thể nhìn thấy biển để đặt biển quảng cáo homestay trên sân thượng, với điều kiện một tòa nhà nhìn được ra biển khi và chỉ khi nó cao hơn mọi tòa nhà đứng giữa nó và bờ biển (phía bên phải). Những tòa bị che khuất hoàn toàn sẽ không được chọn.

## Nhiệm vụ

Cho $N$ số nguyên là chiều cao các tòa nhà từ trái sang phải (biển ở phía bên phải tòa cuối cùng). Hãy lập trình đếm số tòa nhà cao hơn mọi tòa đứng bên phải nó, rồi in ra số lượng đó.

## Input

- Dòng đầu tiên chứa số nguyên $N$ ($1 \le N \le 10^5$), là số tòa nhà.
- Dòng thứ hai chứa $N$ số nguyên $h_i$ ($1 \le h_i \le 10^9$), là chiều cao từng tòa.

## Output

- In ra một số nguyên duy nhất là số tòa nhà nhìn thấy biển.

## Sample 1

### Input

```text
4
4 2 3 1
```

### Output

```text
3
```

### Giải thích

- Xét từ tòa gần biển nhất trở về: tòa cao $1$ không bị ai che nên nhìn thấy biển.
- Tòa cao $3$ cao hơn mọi tòa bên phải nó (chỉ có tòa $1$) nên nhìn thấy biển.
- Tòa cao $2$ thấp hơn tòa $3$ đứng bên phải nên bị che khuất.
- Tòa cao $4$ cao hơn mọi tòa bên phải ($2, 3, 1$) nên nhìn thấy biển.
- Có $3$ tòa nhìn thấy biển.

## Ràng buộc

- $1 \le N \le 10^5$, $1 \le h_i \le 10^9$.
- Thời gian: $1.0\text{s}$, Bộ nhớ: $256\text{MB}$.
