# SosMedGrab API

**SosMedGrab API** adalah Rest api untuk grab informasi dari berbagai sosial media seperti **Instagram**, **TikTok** dan **Youtube**.

---

## Installation

```bash
git clone https://github.com/SukunDev/sosmedgrab-api.git
cd sosmedgrab-api
npm i -g vercel
vercel dev
```

## Rest API

Contoh penggunaan rest api ada di bawah ini

### Request

`POST /instagram`

```bash
curl -i -d "target_url=https://www.instagram.com/reel/C06xLG0I-gv/" http://localhost:3000/instagram
```

### Response

```
HTTP/1.1 200 OK
cache-control: public, max-age=0, must-revalidate
Content-Type: application/json
Content-Length: 2390
Access-Control-Allow-Origin: *
server: Vercel
x-vercel-id: dev1::dev1::111eo-1704546679997-ebf8573449ad
x-vercel-cache: MISS
Date: Sat, 06 Jan 2024 13:11:22 GMT
Connection: keep-alive
Keep-Alive: timeout=5

{
    "status": true,
    "user": {
        "biography": "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Sed do eiusmod tempor incididunt ut labore et dolore magna aliqua.",
        "category name": "Dummy Category",
        "full name": "John Doe",
        "jumlah followers": 5000,
        "jumlah following": 200,
        "jumlah responses": 150,
        "profile picture": "https://dummyimage.com/320x320/000000/ffffff",
        "user id": 1234567890,
        "username": "john.doe"
    },
    "items": [
        {
            "caption": "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. #dummycaption #loremipsum #dummydata",
            "media": {
                "height": 1920,
                "thumbnail": "https://dummyimage.com/480x480/000000/ffffff",
                "type": "image",
                "url": "https://dummyimage.com/1080x720/000000/ffffff"
            },
            "media_id": "12345678901234567890",
            "product_type": "dummy",
            "shortcode": "ABC123"
        }
    ]
}
```

## Kontribusi

Jika Anda ingin berkontribusi pada proyek ini, kami sangat menghargai setiap bentuk dukungan. Silakan buka [Panduan Kontribusi](CONTRIBUTING.md) untuk informasi lebih lanjut.

## Lisensi

Proyek ini dilisensikan di bawah [MIT License](LICENSE).

---

Dikembangkan oleh [SukunDev](https://github.com/SukunDev)
