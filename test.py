import re

# -*- coding: utf-8 -*-
text = '''আমি কোনো ভাষাবিজ্ঞানী নই। তাই ভাষাগত, 
শব্দব্যঞ্জনগত শুদ্ধতা, তাল-লয় -এসব বিষয়ে আমার জ্ঞান খুবই প্রাথমিক। 
তাই এই লেখায় এসব ভাষাবিজ্ঞানগত তাত্ত্বিক উপাদান খুঁজতে যাওয়া অর্থহীন হবে। 
আমি চেষ্টা করেছি বাংলা ভাষায় দীর্ঘ শব্দ রাখতে, তবে তা দীর্ঘতম – এমন দাবি আমি করছি না।'''

outText = text.split();
for i in range(len(outText)):
    print(outText[i])
