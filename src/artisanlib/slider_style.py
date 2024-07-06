artisan_slider_style = """
            QSlider::groove:vertical:focus {{      
                background: #8e8e93;
                border:5px solid #1c1c1e;
                width: 0.1px;
                border-radius: 550px;
            }}
            QSlider::sub-page:vertical:focus {{
                background: #8e8e93;
                border: 0.5px solid #666;
                width: 85px;
                border-radius: 5px;
            }}
            QSlider::groove:vertical {{
                background: #8e8e93;
                border: 5px solid #aaa;
                width: 0.1px;
                border-radius: 5px;
            }}
            QSlider::sub-page:vertical {{
                background: #8e8e93;
                border: 0.5px solid #aaa;
                width: 85px;
                border-radius: 5px;
            }}
            QSlider::add-page:vertical {{
                background: #007aff;
                border: 1px solid #007aff;
                width: 5px;
                border-radius: 20px;
            }}
            QSlider::handle:vertical {{
                background: qlineargradient(x1:0, y1:0, x2:1, y2:1, stop:0 #BDBEC2, stop:1 #BDBEC2);
                border: 0.5px solid #BDBEC2;
                height: 44px;
                margin-top: -1px;
                margin-bottom: -1px;
                margin-left: -24px;
                margin-right: -24px;
                border-radius: 10px;
            }}
            QSlider::handle:vertical:!hover:focus {{
                background: qlineargradient(x1:0, y1:0, x2:1, y2:1, stop:0 #bdbec2, stop:1 #bdbec2);
                border: 1px solid #bdbec2;
                border-radius: 10px;
            }}
            QSlider::handle:vertical:hover:focus {{
                background: qlineargradient(x1:0, y1:0, x2:1, y2:1, stop:0 #007AFF, stop:1 #007AFF);
                border: 1px solid #007AFF;
                border-radius: 10px;
            }}
            QSlider::handle:vertical:hover {{
                background: qlineargradient(x1:0, y1:0, x2:1, y2:1, stop:0 #eee, stop:1 #ddd);
                border: 1px solid #ccc;
                border-radius: 10px;
            }}
            QSlider::sub-page:vertical:disabled {{
                background: #bbb;
                border-color: #999;
            }}
            QSlider::add-page:vertical:disabled {{
                background: #eee;
                border-color: #999;
            }}
            QSlider::handle:vertical:disabled {{
                background: #eee;
                border: 1px solid #aaa;
                border-radius: 10px;
            }}
"""
