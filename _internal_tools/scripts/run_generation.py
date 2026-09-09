import os

from generate_pages import generate_trek_page, get_megamenu_html

treks_data = [
    # --- 1. ANNAPURNA BASE CAMP (ABC) TREKS ---
    {
        "slug": "8-days-annapurna-base-camp-trek",
        "title": "8 Days Annapurna Base Camp Trek",
        "category": "Annapurna Base Camp",
        "duration": "8 Days / 7 Nights",
        "elevation": "4,130m (13,550 ft)",
        "grade": "Moderate-Strenuous",
        "price": "790",
        "image": "https://images.unsplash.com/photo-1544735716-392fe2489ffa?auto=format&fit=crop&w=1200&q=80",
        "headline": "A streamlined 8-day expedition to Annapurna Base Camp starting and concluding at Siwai trailhead.",
        "lead": "The 8 Days Annapurna Base Camp trek offers an efficient route into the heart of the Annapurna Sanctuary, cutting out the lower loop to focus purely on the glacial mountain amphitheater.",
        "overview": "By starting at the roadhead of Siwai (via private 4WD from Pokhara), this itinerary climbs straight up through Chhomrong, Bamboo, and Deurali directly to Machhapuchhre Base Camp (3,700m) and Annapurna Base Camp (4,130m). It provides an ideal balance of fast pacing without sacrificing acclimatization.",
        "highlights": [
            ("Base Camp Amphitheater", "Witness dawn light across the 360-degree snow walls of Annapurna I and Annapurna South."),
            ("Efficient Trailhead Access", "Save 2 days of lower valley walking via private 4WD transit to Siwai."),
            ("Jhinu Hot Springs", "Soothe tired legs in natural riverside hot spring pools on your descent."),
            ("Gurung Hospitality", "Stay in classic Gurung hospitality teahouses in upper Chhomrong and Sinuwa.")
        ],
        "itinerary": [
            {"title": "Drive Pokhara to Siwai (3 hrs), Trek to Chhomrong", "alt": "2,170m", "time": "5.0 hrs", "desc": "Scenic 4WD drive to Siwai trailhead. Ascend through Jhinu Danda to the stone village of Chhomrong.", "note": "Prepare for stone staircases up to Chhomrong. Hydrate well."},
            {"title": "Chhomrong to Dovan through the Bamboo Forest", "alt": "2,600m", "time": "5.5 hrs", "desc": "Descend Chhomrong stone steps, cross suspension bridge, climb to Sinuwa and continue to Dovan."},
            {"title": "Dovan to Deurali via Hinku Cave", "alt": "3,230m", "time": "4.5 hrs", "desc": "Trek through subalpine bamboo and oak forests past the historic rock shelter of Hinku Cave to Deurali."},
            {"title": "Deurali to Machhapuchhre Base Camp (MBC)", "alt": "3,700m", "time": "4.0 hrs", "desc": "Enter the narrow gateway into the Sanctuary. The gorge widens dramatically as you reach MBC.", "note": "Afternoon SpO2 pulse oximetry monitoring conducted by your lead guide."},
            {"title": "MBC to Annapurna Base Camp (ABC 4,130m)", "alt": "4,130m", "time": "2.5 hrs", "desc": "Gentle 2-hour walk into the glacial basin of ABC. Sunset over the south face of Annapurna I (8,091m)."},
            {"title": "Sunrise at ABC, Trek down to Bamboo", "alt": "2,310m", "time": "6.5 hrs", "desc": "Golden sunrise over Annapurna amphitheater. Descend through MBC, Deurali, and Himalaya down to Bamboo."},
            {"title": "Bamboo to Jhinu Danda & Hot Springs", "alt": "1,780m", "time": "5.0 hrs", "desc": "Climb up to Chhomrong for lunch, descend to Jhinu. Afternoon relaxation in riverside hot spring pools."},
            {"title": "Jhinu to Siwai Trailhead, Drive to Pokhara", "alt": "820m", "time": "2.5 hrs walk + 3 hrs drive", "desc": "Cross the long Jhinu suspension bridge to Siwai. Private 4WD transfer back to Pokhara Lakeside."}
        ],
        "faqs": [
            ("Is 8 days enough time to acclimatize?", "Yes, because the route sleeps at Chhomrong (2,170m), Dovan (2,600m), Deurali (3,230m), and MBC (3,700m) before spending the night at ABC (4,130m), following safe elevation gain guidelines."),
            ("Do I need to carry all my bags?", "No. Insured local porters (1 porter per 2 trekkers, max 20kg cap) carry your main duffel bag, leaving you with just a daypack.")
        ]
    },
    {
        "slug": "short-annapurna-base-camp-trek",
        "title": "Short Annapurna Base Camp Trek",
        "category": "Annapurna Base Camp",
        "duration": "6-7 Days",
        "elevation": "4,130m (13,550 ft)",
        "grade": "Strenuous",
        "price": "720",
        "image": "https://images.unsplash.com/photo-1506197603052-3cc9c3a201bd?auto=format&fit=crop&w=1200&q=80",
        "headline": "The fastest safe route to Annapurna Base Camp for experienced, cardio-fit trekkers.",
        "lead": "Designed for fit adventurers with limited vacation time, the Short Annapurna Base Camp Trek condenses the journey into 6 to 7 high-energy trail days with direct trailhead logistics.",
        "overview": "By maximizing trail efficiency and using private 4WD transit directly to Matque/Siwai, this itinerary allows conditioned hikers to reach the 4,130m Annapurna amphitheater and return to Pokhara in under a week.",
        "highlights": [
            ("Fast-Paced Itinerary", "Reach 4,130m and return to Pokhara in only 6 to 7 days."),
            ("Direct Valley Route", "Travel straight through the Modi Khola canyon with no redundant loops."),
            ("High Mountain Amphitheater", "Experience the same awe-inspiring 360° summit views as longer routes."),
            ("Private Transit Included", "Direct private Scorpio 4WD transfers to trailheads minimize road delays.")
        ],
        "itinerary": [
            {"title": "Drive Pokhara to Matque/Siwai, Trek to Sinuwa", "alt": "2,340m", "time": "6.0 hrs", "desc": "Early morning 4WD drive from Pokhara. Trek briskly through Jhinu and Chhomrong up to Sinuwa."},
            {"title": "Sinuwa to Deurali", "alt": "3,230m", "time": "6.5 hrs", "desc": "Long forest hike through Bamboo, Dovan, and Himalaya Hotel up to the alpine outpost of Deurali."},
            {"title": "Deurali to Annapurna Base Camp via MBC", "alt": "4,130m", "time": "5.5 hrs", "desc": "Climb past Machhapuchhre Base Camp into the heart of the Sanctuary at ABC for sunset.", "note": "Strict SpO2 oximeter checks are conducted at lunch and dinner."},
            {"title": "Sunrise at ABC, Long Descent to Bamboo", "alt": "2,310m", "time": "6.5 hrs", "desc": "Sunrise photos at ABC. Descend down through the gorge to Bamboo."},
            {"title": "Bamboo to Jhinu Danda (Hot Springs)", "alt": "1,780m", "time": "5.0 hrs", "desc": "Climb stone stairs to Chhomrong and descend to Jhinu Danda. Hot springs bath."},
            {"title": "Jhinu to Siwai, 4WD Drive to Pokhara", "alt": "820m", "time": "2.5 hrs walk + 3 hrs drive", "desc": "Short morning walk to roadhead, private jeep transfer back to Pokhara Lakeside."}
        ],
        "faqs": [
            ("Who is this trek suitable for?", "This trek is designed for runners, cyclists, and fit hikers who can walk 6-7 hours daily on steep mountain stairs."),
            ("Are permits included?", "Yes, all ACAP conservation area permits, checkpoint fees, and licensed guide services are fully included.")
        ]
    },

    # --- 2. ANNAPURNA CIRCUIT TREKS ---
    {
        "slug": "annapurna-circuit-trek",
        "title": "Annapurna Circuit Trek",
        "category": "Annapurna Circuit",
        "duration": "16-18 Days",
        "elevation": "5,416m (17,769 ft)",
        "grade": "Challenging",
        "price": "1290",
        "image": "https://images.unsplash.com/photo-1585409677983-0f6c41ca9c3b?auto=format&fit=crop&w=1200&q=80",
        "headline": "The complete legendary Himalayan crossing over the 5,416m Thorong La Pass.",
        "lead": "The Annapurna Circuit is widely celebrated as one of the world's greatest long-distance mountain treks, encircling the entire Annapurna Massif through distinct ecological zones.",
        "overview": "From the subtropical lowlands of Lamjung, the trail climbs alongside the Marsyangdi River through Tibetan Buddhist settlements in Manang, crosses the high glacial barrier of Thorong La Pass (5,416m), and drops into the sacred rain-shadow desert of Mustang and Muktinath.",
        "highlights": [
            ("Thorong La Pass (5,416m)", "Cross one of the highest navigable trekking mountain passes in the world."),
            ("Manang Cultural Immersion", "Spend acclimatization days exploring 500-year-old Buddhist monasteries and cliffside caves."),
            ("Two Contrasting Worlds", "Transition from green subtropical gorges into the arid Tibetan-plateau desert of Mustang."),
            ("Sacred Muktinath Temple", "Visit the holy pilgrimage site sacred to both Hindus and Buddhists.")
        ],
        "itinerary": [
            {"title": "Drive Kathmandu / Pokhara to Besisahar & Dharapani", "alt": "1,860m", "time": "7-8 hrs drive", "desc": "Scenic drive into the Marsyangdi River valley, entering the Annapurna Conservation Area."},
            {"title": "Dharapani to Chame", "alt": "2,670m", "time": "5.5 hrs", "desc": "Trek through pine and oak forests into the district headquarters of Manang at Chame."},
            {"title": "Chame to Upper Pisang", "alt": "3,300m", "time": "5.0 hrs", "desc": "Witness the dramatic Paungda Danda curved rock face and stunning views of Annapurna II."},
            {"title": "Upper Pisang to Manang via Ghyaru & Ngawal", "alt": "3,540m", "time": "6.5 hrs", "desc": "Spectacular high-route overlooking the broad Manang valley and Annapurna III and IV."},
            {"title": "Acclimatization & Exploration Day in Manang", "alt": "3,540m", "time": "Rest / Hike", "desc": "Day hike to Gangapurna glacial lake or Praken Gompa for high-altitude acclimatization.", "note": "Hydrate well and practice slow breathing. Oximeter checks conducted."},
            {"title": "Manang to Yak Kharka", "alt": "4,050m", "time": "4.0 hrs", "desc": "Gentle climb above the tree line into alpine pastures where blue sheep and yaks graze."},
            {"title": "Yak Kharka to Thorong Phedi / High Camp", "alt": "4,525m", "time": "4.5 hrs", "desc": "Ascend to the foot of Thorong La Pass. Rest early in preparation for the high pass crossing."},
            {"title": "Cross Thorong La Pass (5,416m), Descend to Muktinath", "alt": "3,800m", "time": "8-9 hrs", "desc": "Pre-dawn 4 AM departure. Reach the prayer-flag-strewn summit of Thorong La Pass (5,416m). Long descent to Muktinath.", "note": "Crucial day. Microspikes and warm windproof layers mandatory."},
            {"title": "Muktinath to Jomsom via Kagbeni & Kali Gandaki", "alt": "2,720m", "time": "5.5 hrs", "desc": "Trek through the windy Kali Gandaki gorge past ancient Mustang villages to Jomsom."},
            {"title": "Fly or Drive Jomsom to Pokhara", "alt": "820m", "time": "25 min flight / drive", "desc": "Scenic morning flight between Annapurna and Dhaulagiri peaks back to Pokhara Lakeside."}
        ],
        "faqs": [
            ("How difficult is Thorong La Pass?", "Thorong La is challenging due to the high elevation (5,416m) and early morning sub-zero temperatures, but does not require technical mountaineering skills."),
            ("Are permits included?", "Yes, both the ACAP permit and TIMS registration are fully arranged and included.")
        ]
    },
    {
        "slug": "14-days-annapurna-circuit-trek",
        "title": "14 Days Annapurna Circuit Trek",
        "category": "Annapurna Circuit",
        "duration": "14 Days / 13 Nights",
        "elevation": "5,416m (17,769 ft)",
        "grade": "Challenging",
        "price": "1180",
        "image": "https://images.unsplash.com/photo-1585409677983-0f6c41ca9c3b?auto=format&fit=crop&w=1200&q=80",
        "headline": "The modernized 2-week Annapurna Circuit itinerary crossing the mighty Thorong La Pass.",
        "lead": "This 14-day Annapurna Circuit itinerary cuts out road-walking sections by utilizing private 4WD transit to Chame, providing the ideal timeframe for modern travelers to conquer Thorong La Pass.",
        "overview": "Focusing on the highest, most scenic alpine sections of the circuit, this route preserves vital acclimatization days in Manang while delivering the ultimate thrill of standing at 5,416m before descending into Mustang.",
        "highlights": [
            ("14-Day Optimized Schedule", "Full circuit highlights without wasting days on lower dirt roads."),
            ("Thorong La Summit (5,416m)", "The ultimate Himalayan high-pass crossing experience."),
            ("Manang Cultural Immersion", "Traditional stone villages, stupas, and Tibetan Buddhism."),
            ("Kali Gandaki Valley", "Descend into the deepest river canyon on earth.")
        ],
        "itinerary": [
            {"title": "Drive Kathmandu to Besisahar & Chame", "alt": "2,670m", "time": "8 hrs drive", "desc": "Private 4WD transit up the rugged Marsyangdi gorge directly to Chame."},
            {"title": "Chame to Pisang", "alt": "3,200m", "time": "5.0 hrs", "desc": "Trek through pine forests beneath the colossal stone face of Paungda Danda."},
            {"title": "Pisang to Manang via Upper Route", "alt": "3,540m", "time": "6.0 hrs", "desc": "Panoramic high trail offering awe-inspiring vistas of Annapurna II, III, and IV."},
            {"title": "Acclimatization Day in Manang", "alt": "3,540m", "time": "Rest day", "desc": "Short hikes to Gangapurna Lake and Ice Lake viewpoint for altitude adaptation."},
            {"title": "Manang to Yak Kharka", "alt": "4,050m", "time": "4.0 hrs", "desc": "Ascend above treeline through barren alpine meadows dotted with yak pastures."},
            {"title": "Yak Kharka to Thorong Phedi", "alt": "4,525m", "time": "4.0 hrs", "desc": "Base camp for the Thorong La crossing. Rest and early dinner."},
            {"title": "Thorong Phedi to Thorong La (5,416m) to Muktinath", "alt": "3,800m", "time": "8.5 hrs", "desc": "Ascent to the pass at dawn. Incredible views across the Annapurnas and Tibetan ranges. Descend to holy Muktinath."},
            {"title": "Muktinath to Jomsom", "alt": "2,720m", "time": "5.0 hrs", "desc": "Trek through the wind-carved Kali Gandaki valley to Jomsom."},
            {"title": "Flight / Drive Jomsom to Pokhara", "alt": "820m", "time": "Transit", "desc": "Scenic morning flight past Dhaulagiri into the subtropical warmth of Pokhara."}
        ],
        "faqs": [
            ("Can I do this route in 14 days without rushing?", "Yes. By utilizing private 4WD transit to Chame, the high mountain walking and acclimatization schedule is identical to the classic 18-day route."),
            ("What gear is needed for Thorong La?", "Microspikes, windproof outer shells, thermal base layers, and a -15°C down jacket are mandatory.")
        ]
    },
    {
        "slug": "annapurna-circuit-short-trek",
        "title": "Annapurna Circuit Short Trek",
        "category": "Annapurna Circuit",
        "duration": "10-11 Days",
        "elevation": "5,416m (17,769 ft)",
        "grade": "Challenging",
        "price": "990",
        "image": "https://images.unsplash.com/photo-1585409677983-0f6c41ca9c3b?auto=format&fit=crop&w=1200&q=80",
        "headline": "A fast-paced, high-altitude sprint over Thorong La Pass for experienced trekkers.",
        "lead": "The Annapurna Circuit Short Trek is tailored for seasoned hikers who want the legendary challenge of Thorong La Pass (5,416m) in 10 to 11 days.",
        "overview": "By utilizing 4WD transport to Upper Pisang and domestic flights from Jomsom to Pokhara, this trek strips out lower-elevation walking while preserving essential safety days in Manang.",
        "highlights": [
            ("Time-Efficient Thorong La", "Conquer the world's most famous trekking pass in 10 days."),
            ("Manang & Tibetan Enclaves", "Rich Buddhist culture and dry alpine landscapes."),
            ("Flight from Jomsom", "Breathtaking mountain flight down the Kali Gandaki gorge."),
            ("Private 4WD Logistics", "Fast trailhead transfers minimize transit fatigue.")
        ],
        "itinerary": [
            {"title": "Drive Kathmandu to Besisahar & Pisang", "alt": "3,200m", "time": "Full day drive", "desc": "Long 4WD drive up into high Manang district."},
            {"title": "Pisang to Manang", "alt": "3,540m", "time": "5.0 hrs", "desc": "Trek through the pine-scented Manang basin with Annapurna views."},
            {"title": "Acclimatization Day in Manang", "alt": "3,540m", "time": "Active Rest", "desc": "Hike to Gangapurna Glacier for altitude adaptation."},
            {"title": "Manang to Yak Kharka", "alt": "4,050m", "time": "4.0 hrs", "desc": "Trek past juniper trees to the alpine hamlet of Yak Kharka."},
            {"title": "Yak Kharka to Thorong High Camp", "alt": "4,850m", "time": "4.5 hrs", "desc": "Climb steeply to high camp below the pass."},
            {"title": "Thorong High Camp to Thorong La (5,416m) to Muktinath", "alt": "3,800m", "time": "8.0 hrs", "desc": "Early morning pass crossing, epic panoramic photography, descent to Muktinath."},
            {"title": "Muktinath to Jomsom, Fly to Pokhara", "alt": "820m", "time": "Transit", "desc": "Short morning drive to Jomsom airport, scenic mountain flight to Pokhara."}
        ],
        "faqs": [
            ("Is this safe for beginners?", "No, the Short Circuit is recommended only for experienced hikers who acclimatize quickly and have prior high-altitude experience.")
        ]
    },
    {
        "slug": "annapurna-circuit-with-tilicho-lake-trek",
        "title": "Annapurna Circuit with Tilicho Lake Trek",
        "category": "Annapurna Circuit",
        "duration": "16 Days / 15 Nights",
        "elevation": "5,416m (Pass) / 4,919m (Lake)",
        "grade": "Challenging / Strenuous",
        "price": "1390",
        "image": "https://images.unsplash.com/photo-1544735716-392fe2489ffa?auto=format&fit=crop&w=1200&q=80",
        "headline": "The ultimate Himalayan grand tour combining turquoise Tilicho Lake with Thorong La Pass.",
        "lead": "This expedition incorporates a dramatic side-trip to Tilicho Lake (4,919m)—one of the highest alpine glacial lakes on earth—before crossing the mighty Thorong La Pass.",
        "overview": "Set beneath the sheer glaciated cliffs of the 'Great Barrier', Tilicho Lake is a deep turquoise jewel. Visiting Tilicho before Thorong La provides unmatched acclimatization, making the pass crossing significantly easier and more enjoyable.",
        "highlights": [
            ("Tilicho Lake (4,919m)", "Stand on the icy shores of one of the world's highest glacial lakes."),
            ("The Great Barrier", "Walk beneath the legendary vertical snow wall discovered by Maurice Herzog."),
            ("Thorong La Pass (5,416m)", "Cross the iconic high pass with superior acclimatization."),
            ("Complete Alpine Immersion", "Experience two of Nepal's most revered mountain landmarks in one journey.")
        ],
        "itinerary": [
            {"title": "Drive Kathmandu to Chame", "alt": "2,670m", "time": "8 hrs drive", "desc": "4WD transit up the dramatic Marsyangdi river canyon."},
            {"title": "Chame to Pisang to Manang", "alt": "3,540m", "time": "2 days trek", "desc": "Ascend into the dry pine forests and broad valley of Manang."},
            {"title": "Manang to Siri Kharka", "alt": "4,060m", "time": "5.0 hrs", "desc": "Leave the main circuit trail and hike west toward Tilicho through Khangsar village."},
            {"title": "Siri Kharka to Tilicho Base Camp", "alt": "4,150m", "time": "5.5 hrs", "desc": "Walk along dramatic landslide scree trails carved into the mountain cliffs."},
            {"title": "Hike to Tilicho Lake (4,919m), Return to Siri Kharka", "alt": "4,919m / 4,060m", "time": "7.5 hrs", "desc": "Early morning ascent to the frozen blue expanse of Tilicho Lake beneath the Great Barrier."},
            {"title": "Siri Kharka to Yak Kharka", "alt": "4,050m", "time": "5.0 hrs", "desc": "Rejoin the main circuit trail heading toward Thorong La."},
            {"title": "Yak Kharka to Thorong High Camp", "alt": "4,850m", "time": "4.5 hrs", "desc": "Final staging camp before the pass."},
            {"title": "Cross Thorong La Pass (5,416m) to Muktinath", "alt": "3,800m", "time": "8.5 hrs", "desc": "Trek over the summit of Thorong La with magnificent panoramic Himalayan views."},
            {"title": "Muktinath to Jomsom, Flight to Pokhara", "alt": "820m", "time": "Transit", "desc": "Drive through Mustang to Jomsom, flight to Pokhara."}
        ],
        "faqs": [
            ("How is the trail to Tilicho Lake?", "The trail crosses exposed scree slopes that require sure footing, but is non-technical and well-trodden during trekking seasons."),
            ("Does Tilicho help with Thorong La?", "Yes, spending time at 4,919m at Tilicho Lake acts as the ultimate acclimatization booster before tackling 5,416m at Thorong La.")
        ]
    },

    # --- 3. POON HILL / GHOREPANI TREKS ---
    {
        "slug": "ghorepani-poon-hill-trek",
        "title": "Ghorepani Poonhill Trek",
        "category": "Poon Hill / Ghorepani",
        "duration": "4-5 Days",
        "elevation": "3,210m (10,531 ft)",
        "grade": "Easy-Moderate",
        "price": "450",
        "image": "https://images.unsplash.com/photo-1516483638261-f4dbaf036963?auto=format&fit=crop&w=1200&q=80",
        "headline": "Nepal's most famous introductory Himalayan sunrise trek with sweeping Dhaulagiri views.",
        "lead": "The Ghorepani Poon Hill trek is the quintessential introductory trek in Nepal, offering world-class sunrise views over Dhaulagiri and Annapurna without high altitude sickness risk.",
        "overview": "Winding through ancient rhododendron forests, Gurung and Magar stone villages, and ascending the stone steps of Ulleri, this trek culminates at dawn on Poon Hill (3,210m) where the rising sun illuminates over thirty Himalayan peaks.",
        "highlights": [
            ("Poon Hill Sunrise (3,210m)", "World-renowned panorama of Dhaulagiri I (8,167m), Annapurna I, and Machhapuchhre."),
            ("Spring Rhododendron Bloom", "Trek through the largest natural rhododendron forest in the world during March-April."),
            ("Ghandruk Cultural Heritage", "Explore the stone-paved Gurung cultural village with local museums."),
            ("Accessible & Family-Friendly", "Gentle altitudes suitable for first-timers, families, and short getaways.")
        ],
        "itinerary": [
            {"title": "Drive Pokhara to Nayapul / Birethanti, Trek to Tikhedhunga", "alt": "1,540m", "time": "1.5 hrs drive + 4 hrs walk", "desc": "Follow the sub-tropical river valley past terraced farmlands."},
            {"title": "Tikhedhunga to Ghorepani via Ulleri Stairs", "alt": "2,860m", "time": "5.5 hrs", "desc": "Climb the 3,300 stone steps of Ulleri and continue through mossy rhododendron forests to Ghorepani."},
            {"title": "Poon Hill Sunrise (3,210m), Trek to Tadapani", "alt": "2,630m", "time": "6.0 hrs", "desc": "Dawn hike to Poon Hill for 360° Himalayan sunrise. Breakfast, then trek along forested ridges to Tadapani."},
            {"title": "Tadapani to Ghandruk, Drive to Pokhara", "alt": "820m", "time": "3.5 hrs walk + 2 hrs drive", "desc": "Descend to the picturesque Gurung stone village of Ghandruk. Transfer by private vehicle to Pokhara."}
        ],
        "faqs": [
            ("Is Poon Hill suitable for children and seniors?", "Yes, because maximum sleeping elevation is only 2,860m at Ghorepani, altitude sickness is very rare."),
            ("When is the best season for Poon Hill?", "Autumn (October–November) offers crystal-clear skies, while Spring (March–April) brings explosive rhododendron blooms.")
        ]
    },
    {
        "slug": "3-days-poon-hill-trek",
        "title": "3 Days PoonHill Trek",
        "category": "Poon Hill / Ghorepani",
        "duration": "3 Days / 2 Nights",
        "elevation": "3,210m (10,531 ft)",
        "grade": "Moderate",
        "price": "360",
        "image": "https://images.unsplash.com/photo-1516483638261-f4dbaf036963?auto=format&fit=crop&w=1200&q=80",
        "headline": "The fastest 3-day express sunrise getaway to Poon Hill from Pokhara.",
        "lead": "Short on time in Nepal? The 3 Days Poon Hill Trek delivers the complete Himalayan sunrise experience in just a long weekend.",
        "overview": "Utilizing private 4WD transit from Pokhara to the high trailhead above Tikhedhunga, this route allows you to reach Ghorepani on Day 1, catch the famous Poon Hill sunrise on Day 2, and return to Pokhara on Day 3.",
        "highlights": [
            ("Poon Hill Sunrise (3,210m)", "Panoramic mountain dawn across Dhaulagiri and the Annapurnas."),
            ("Express 3-Day Timeline", "Ideal for travelers spending just a weekend in Pokhara."),
            ("Rhododendron Forest Trail", "Walk through primeval high-altitude forests."),
            ("Private Jeep Transfers", "Direct trailhead transfers maximize your hiking efficiency.")
        ],
        "itinerary": [
            {"title": "Drive Pokhara to Ulleri roadhead, Trek to Ghorepani", "alt": "2,860m", "time": "3 hrs drive + 4 hrs walk", "desc": "Drive past Nayapul up to Ulleri. Trek through rhododendron forests to Ghorepani."},
            {"title": "Poon Hill Sunrise (3,210m), Trek to Ghandruk", "alt": "1,940m", "time": "6.0 hrs", "desc": "Sunrise at Poon Hill, breakfast in Ghorepani, then hike through Tadapani down to Ghandruk."},
            {"title": "Explore Ghandruk, Drive to Pokhara", "alt": "820m", "time": "2 hrs walk + 2.5 hrs drive", "desc": "Visit Gurung museum, descend to roadhead, private jeep transfer back to Pokhara Lakeside."}
        ],
        "faqs": [
            ("How fit do I need to be for the 3-day trek?", "A basic level of cardiovascular fitness is required, as the hiking days are steady (4-6 hours).")
        ]
    },
    {
        "slug": "4-days-poon-hill-trek",
        "title": "4 Days PoonHill Trek",
        "category": "Poon Hill / Ghorepani",
        "duration": "4 Days / 3 Nights",
        "elevation": "3,210m (10,531 ft)",
        "grade": "Easy-Moderate",
        "price": "420",
        "image": "https://images.unsplash.com/photo-1516483638261-f4dbaf036963?auto=format&fit=crop&w=1200&q=80",
        "headline": "The classic, perfectly paced 4-day Poon Hill circuit from Pokhara.",
        "lead": "The 4 Days Poon Hill Trek is the gold-standard short trek in the Annapurna region, providing the ideal balance of scenic trail walking and cultural village rest.",
        "overview": "Starting at Nayapul, you ascend the historic stone staircases of Ulleri, stay in mountain lodges in Ghorepani, witness dawn from Poon Hill, and descend via Tadapani and Ghandruk.",
        "highlights": [
            ("Poon Hill Golden Hour", "Iconic sunrise illuminating over thirty 7,000m and 8,000m peaks."),
            ("Ghandruk Village", "Traditional stone houses and Gurung cultural hospitality."),
            ("Ulleri Staircase", "A classic Himalayan trekking milestone through Magar settlements."),
            ("Comfortable Teahouses", "Cozy lodges with hot meals, bakery treats, and Wi-Fi.")
        ],
        "itinerary": [
            {"title": "Drive Pokhara to Nayapul, Trek to Tikhedhunga", "alt": "1,540m", "time": "1.5 hrs drive + 4.5 hrs walk", "desc": "Drive from Pokhara Lakeside to trailhead. Follow river trails to Tikhedhunga."},
            {"title": "Tikhedhunga to Ghorepani", "alt": "2,860m", "time": "5.5 hrs", "desc": "Ascend Ulleri stone staircase and walk through enchanted rhododendron woodlands."},
            {"title": "Poon Hill Sunrise (3,210m), Trek to Tadapani", "alt": "2,630m", "time": "5.5 hrs", "desc": "Sunrise over Annapurna and Dhaulagiri. Trek through scenic mountain ridges."},
            {"title": "Tadapani to Ghandruk, Drive to Pokhara", "alt": "820m", "time": "3.5 hrs walk + 2 hrs drive", "desc": "Descend to Ghandruk village for lunch, transfer by private jeep to Pokhara."}
        ],
        "faqs": [
            ("What permits are required?", "The Annapurna Conservation Area Permit (ACAP) is required and is fully included in our tour package.")
        ]
    },
    {
        "slug": "5-days-poon-hill-trek",
        "title": "5 Day PoonHill Trek",
        "category": "Poon Hill / Ghorepani",
        "duration": "5 Days / 4 Nights",
        "elevation": "3,210m (10,531 ft)",
        "grade": "Easy-Moderate",
        "price": "490",
        "image": "https://images.unsplash.com/photo-1516483638261-f4dbaf036963?auto=format&fit=crop&w=1200&q=80",
        "headline": "A relaxed, immersive 5-day cultural and scenic loop through Ghorepani and Ghandruk.",
        "lead": "With an extra night in the Gurung heritage capital of Ghandruk, the 5 Day Poon Hill Trek offers a leisurely pace ideal for photographers, families, and cultural enthusiasts.",
        "overview": "Enjoy shorter daily walking hours, lingering lunch stops, full cultural immersion in Gurung villages, and unhurried time at the Poon Hill vantage point.",
        "highlights": [
            ("Poon Hill Sunrise Vantage", "Spectacular dawn across Dhaulagiri, Annapurna South, and Fishtail."),
            ("Dedicated Ghandruk Stay", "Overnight stay in Ghandruk with visits to local textile weaving and heritage museums."),
            ("Relaxed Walking Hours", "Only 4 to 5 hours of walking per day, leaving afternoons free to relax."),
            ("Rich Himalayan Flora", "Magnificent birds, orchids, and rhododendrons.")
        ],
        "itinerary": [
            {"title": "Drive Pokhara to Birethanti, Trek to Hile", "alt": "1,430m", "time": "1.5 hrs drive + 3.5 hrs walk", "desc": "Gentle introductory walk through terraced rice fields along the river."},
            {"title": "Hile to Ghorepani", "alt": "2,860m", "time": "5.5 hrs", "desc": "Climb Ulleri stairs and ascend through shady forest trails to Ghorepani pass."},
            {"title": "Poon Hill Sunrise (3,210m), Trek to Tadapani", "alt": "2,630m", "time": "5.5 hrs", "desc": "Dawn panorama at Poon Hill, followed by forest ridge trekking to Tadapani."},
            {"title": "Tadapani to Ghandruk Heritage Village", "alt": "1,940m", "time": "3.5 hrs", "desc": "Easy downhill walk to Ghandruk. Afternoon spent exploring traditional stone alleys."},
            {"title": "Ghandruk to Nayapul, Drive to Pokhara", "alt": "820m", "time": "3.5 hrs walk + 1.5 hrs drive", "desc": "Scenic descent through river valleys, private 4WD return to Pokhara Lakeside."}
        ],
        "faqs": [
            ("Is this good for first-time hikers?", "Yes, this is one of the most accessible, enjoyable introductory treks in all of Nepal.")
        ]
    },

    # --- 4. MARDI HIMAL TREKS ---
    {
        "slug": "mardi-himal-trek",
        "title": "Mardi Himal Trek",
        "category": "Mardi Himal",
        "duration": "5-7 Days",
        "elevation": "4,500m (Base Camp) / 3,580m (High Camp)",
        "grade": "Moderate",
        "price": "580",
        "image": "https://images.unsplash.com/photo-1544735716-392fe2489ffa?auto=format&fit=crop&w=1200&q=80",
        "headline": "A breathtaking high-ridge trek walking directly beneath the sacred peak of Machhapuchhre.",
        "lead": "The Mardi Himal Trek is the rising star of the Annapurna region—a pristine ridge-line walk offering intimate, face-to-face vistas of Fishtail Mountain and Annapurna South.",
        "overview": "Unlike valley-floor treks, the Mardi trail climbs along a narrow forested ridge. Once you break above the tree line at Badal Danda (Cloud Ridge), you walk along open alpine meadows with deep valley drop-offs on both sides, culminating at the Mardi Himal Viewpoint (4,200m) and Base Camp (4,500m).",
        "highlights": [
            ("Unrivaled Machhapuchhre Views", "Stand closer to sacred Fishtail Mountain (6,993m) than on any other trail."),
            ("Ridge-Line Walking", "Spectacular ridge walking above cloud inversions with panoramic drop-offs."),
            ("Pristine Forest Camps", "Trek through quiet moss-draped forests of oak, maple, and rhododendron."),
            ("Lesser-Crowded Trail", "A quieter, more tranquil alternative to the classic Annapurna Base Camp route.")
        ],
        "itinerary": [
            {"title": "Drive Pokhara to Kande (1 hr), Trek to Forest Camp", "alt": "2,550m", "time": "1 hr drive + 5.5 hrs walk", "desc": "Climb past Australian Camp and Pothana into dense pristine forests to Forest Camp."},
            {"title": "Forest Camp to Low Camp", "alt": "2,970m", "time": "4.5 hrs", "desc": "Ascend through mossy woodlands. Glimpses of Machhapuchhre begin appearing through the canopy."},
            {"title": "Low Camp to Badal Danda to High Camp", "alt": "3,580m", "time": "4.5 hrs", "desc": "Break out of the tree line onto open grassy ridge. Incredible 360° panoramas at High Camp.", "note": "High Camp is cold and windy. Layer with windproof shells and down jackets."},
            {"title": "High Camp to Mardi Base Camp (4,500m), Descend to Badal Danda", "alt": "4,500m / 3,210m", "time": "7.0 hrs", "desc": "Pre-dawn 4 AM ridge hike to Mardi Himal Viewpoint (4,200m) and Base Camp (4,500m). Unbelievable morning light."},
            {"title": "Badal Danda to Siding Village, Drive to Pokhara", "alt": "820m", "time": "4 hrs walk + 2.5 hrs drive", "desc": "Descend off the ridge into traditional village of Siding. Private 4WD transfer back to Pokhara."}
        ],
        "faqs": [
            ("How does Mardi Himal compare to ABC?", "Mardi Himal is a high-ridge walk with sweeping vistas of Machhapuchhre, while ABC is an enclosed glacial basin surrounded by peaks. Mardi is generally shorter (5-6 days)."),
            ("Is altitude sickness a risk on Mardi Himal?", "Yes, because High Camp is at 3,580m and the viewpoint reaches 4,200m–4,500m. Our guides monitor SpO2 levels and pace the ascent safely.")
        ]
    },

    # --- 5. SPECIALIZED / REMOTE TREKS ---
    {
        "slug": "nar-phu-valley-trek",
        "title": "Nar Phu Valley Trek",
        "category": "Specialized & Remote",
        "duration": "12-14 Days",
        "elevation": "5,320m (Kang La Pass)",
        "grade": "Challenging",
        "price": "1590",
        "image": "https://images.unsplash.com/photo-1526772662000-3f88f10405ff?auto=format&fit=crop&w=1200&q=80",
        "headline": "A restricted medieval Tibetan valley trek of ancient stone villages, glaciers, and high passes.",
        "lead": "Tucked between Annapurna and Manaslu, the Nar Phu Valley is a restricted Himalayan wilderness that feels frozen in the 14th century.",
        "overview": "Requiring a special Restricted Area Permit, Nar Phu takes you off the Annapurna Circuit into remote stone-walled Tibetan fortresses, untouched Buddhist gompas, deep slot canyons, and culminates with crossing the alpine Kang La Pass (5,320m) into Manang.",
        "highlights": [
            ("Restricted Himalayan Enclave", "Only a limited number of travelers are permitted to enter each year."),
            ("Ancient Medieval Villages", "Explore Nar and Phu—mud-brick and stone villages untouched by modern roads."),
            ("Kang La Pass (5,320m)", "Challenging high alpine pass with vistas across the northern face of Annapurna II."),
            ("Tibetan Buddhist Culture", "Centuries-old monasteries, yak caravans, and authentic nomadic culture.")
        ],
        "itinerary": [
            {"title": "Drive Kathmandu to Besisahar & Koto", "alt": "2,600m", "time": "8 hrs drive", "desc": "Enter the Annapurna Conservation Area and stay at the Nar Phu checkpoint gate of Koto."},
            {"title": "Koto to Meta through Narrow River Canyon", "alt": "3,560m", "time": "6.5 hrs", "desc": "Cross the police checkpoint into restricted Nar Phu territory. Walk through towering waterfalls and pine gorges."},
            {"title": "Meta to Phu Village", "alt": "4,080m", "time": "6.5 hrs", "desc": "Trek through desolate desert valleys and ancient chortens to the medieval fortress village of Phu."},
            {"title": "Acclimatization & Exploration in Phu", "alt": "4,080m", "time": "Rest day", "desc": "Visit the sacred Tashi Lhakhang Gompa and meet local Tibetan-descent herders."},
            {"title": "Phu to Nar Phedi & Nar Village", "alt": "4,110m", "time": "6.0 hrs", "desc": "Trek across suspension bridges to the stone village of Nar with terraced barley fields."},
            {"title": "Nar to Kang La Pass (5,320m) to Ngawal", "alt": "3,660m", "time": "8.5 hrs", "desc": "Pre-dawn climb over the snowy Kang La Pass with sweeping views of the entire Annapurna range. Descend to Ngawal."},
            {"title": "Ngawal to Pisang & Drive to Pokhara", "alt": "820m", "time": "Transit", "desc": "Rejoin the Marsyangdi valley and transfer by private 4WD to Pokhara Lakeside."}
        ],
        "faqs": [
            ("What permits are needed for Nar Phu?", "A Special Restricted Area Permit ($100/week in Autumn, $75/week in Spring) plus the standard ACAP permit and a licensed guide are legally required."),
            ("How are teahouses in Nar Phu?", "Teahouses in Nar Phu are basic, authentic community homestays with simple twin rooms and home-cooked meals.")
        ]
    },
    {
        "slug": "khopra-ridge-trek",
        "title": "Khopra Ridge Trek",
        "category": "Specialized & Remote",
        "duration": "9-11 Days",
        "elevation": "4,660m (Khayar Lake) / 3,660m (Ridge)",
        "grade": "Moderate-Strenuous",
        "price": "790",
        "image": "https://images.unsplash.com/photo-1544735716-392fe2489ffa?auto=format&fit=crop&w=1200&q=80",
        "headline": "The best off-the-beaten-path alternative to Poon Hill with jaw-dropping Dhaulagiri views.",
        "lead": "The Khopra Ridge (Khopra Danda) Trek takes you off crowded trails to a high balcony ridge directly opposite the gargantuan south face of Dhaulagiri (8,167m).",
        "overview": "Featuring community-owned eco-lodges whose proceeds support local village schools, this route climbs above the tree line to Khopra Danda (3,660m) with an optional day hike to the sacred alpine waters of Khayar Lake (4,660m).",
        "highlights": [
            ("Face-to-Face with Dhaulagiri", "Arguably the most dramatic close-up vantage of Dhaulagiri I (8,167m) in Nepal."),
            ("Sacred Khayar Lake (4,660m)", "High-altitude pilgrimage glacial lake tucked under Annapurna South."),
            ("Community Eco-Lodges", "Directly support local Magar village schools and community development."),
            ("Pristine Solitude", "Walk through untouched rhododendron forests with a fraction of Poon Hill crowds.")
        ],
        "itinerary": [
            {"title": "Drive Pokhara to Nayapul, Trek to Ghandruk", "alt": "1,940m", "time": "5.0 hrs", "desc": "Scenic drive and climb up to the stone village of Ghandruk."},
            {"title": "Ghandruk to Tadapani to Dobato", "alt": "3,420m", "time": "6.0 hrs", "desc": "Leave tourist trails and climb through pristine forests up to Dobato ridge."},
            {"title": "Dobato to Khopra Danda Ridge", "alt": "3,660m", "time": "5.5 hrs", "desc": "Spectacular ridge walk above clouds with Dhaulagiri dominating the horizon."},
            {"title": "Day Hike to Khayar Lake (4,660m)", "alt": "4,660m", "time": "7.5 hrs", "desc": "Optional day hike to the sacred alpine lake beneath Annapurna South. Return to Khopra."},
            {"title": "Khopra Danda to Swanta Village", "alt": "2,200m", "time": "4.5 hrs", "desc": "Descend off the ridge to the peaceful traditional farming village of Swanta."},
            {"title": "Swanta to Ghorepani / Mohare to Pokhara", "alt": "820m", "time": "Transit", "desc": "Scenic return through forest trails to roadhead and private drive back to Pokhara."}
        ],
        "faqs": [
            ("Are teahouses available on Khopra Ridge?", "Yes, community-owned eco-lodges provide cozy rooms, hot dining halls, and wholesome meals.")
        ]
    },
    {
        "slug": "panchase-trek",
        "title": "Panchase Trek",
        "category": "Specialized & Remote",
        "duration": "3-4 Days",
        "elevation": "2,500m (Panchase Peak)",
        "grade": "Easy",
        "price": "340",
        "image": "https://images.unsplash.com/photo-1526772662000-3f88f10405ff?auto=format&fit=crop&w=1200&q=80",
        "headline": "A gentle, culturally rich eco-trek through pristine rhododendron forests near Pokhara.",
        "lead": "The Panchase Trek is an enchanting low-altitude ridge trek starting directly from Phewa Lake, perfect for nature lovers and families seeking wilderness without altitude stress.",
        "overview": "Traversing through sacred oak and rhododendron forests home to over a hundred species of wild orchids, Panchase Peak (2,500m) offers sunrise panoramas across Dhaulagiri, Annapurna, and Manaslu.",
        "highlights": [
            ("Panchase Peak Viewpoint (2,500m)", "Sunrise views of three 8,000-meter peaks: Dhaulagiri, Annapurna I, and Manaslu."),
            ("Wild Orchid Sanctuary", "Trek through forests famous for rare botanical species and birdlife."),
            ("Authentic Homestays", "Experience warm hospitality in Gurung, Brahmin, and Chhetri farming villages."),
            ("Zero Altitude Sickness Risk", "Max sleeping elevation is under 2,100m, suitable for all ages.")
        ],
        "itinerary": [
            {"title": "Boat across Phewa Lake, Trek to Bhumdi", "alt": "1,520m", "time": "4.0 hrs", "desc": "Row across Phewa Lake from Pokhara Lakeside, hike past Peace Pagoda to Bhumdi village."},
            {"title": "Bhumdi to Panchase Bhanjyang", "alt": "2,060m", "time": "5.5 hrs", "desc": "Walk through lush forest ridges filled with wild orchids and mountain vistas."},
            {"title": "Sunrise at Panchase Peak (2,500m), Trek to Bhadaure", "alt": "1,670m", "time": "5.0 hrs", "desc": "Morning hike to the holy shrine on Panchase Peak. Descend to the traditional village of Bhadaure."},
            {"title": "Bhadaure to Kande, Drive to Pokhara", "alt": "820m", "time": "3.0 hrs walk + 1 hr drive", "desc": "Gentle walk through farming fields, transfer back to Pokhara Lakeside."}
        ],
        "faqs": [
            ("Is this suitable for beginner hikers?", "Yes, Panchase is one of the easiest and most picturesque beginner treks in Nepal.")
        ]
    },
    {
        "slug": "sikles-trek",
        "title": "Sikles Trek",
        "category": "Specialized & Remote",
        "duration": "4-5 Days",
        "elevation": "2,000m (Sikles Village)",
        "grade": "Easy-Moderate",
        "price": "390",
        "image": "https://images.unsplash.com/photo-1526772662000-3f88f10405ff?auto=format&fit=crop&w=1200&q=80",
        "headline": "An authentic cultural journey into one of the largest traditional Gurung villages in Nepal.",
        "lead": "Perched on a mountain terrace directly beneath the towering south face of Annapurna II and IV, Sikles is a living museum of Gurung culture.",
        "overview": "This eco-trek takes you off standard commercial trekking highways into stone-slate-roofed alleyways, where traditional shamanic animism, Gurkha military traditions, and honey-hunting history flourish.",
        "highlights": [
            ("Authentic Gurung Capital", "Explore stone alleys, traditional slate roofs, and Gurung weavers in Sikles."),
            ("Annapurna II & IV Views", "Unobstructed close-up vistas of Annapurna II (7,937m) and Lamjung Himal."),
            ("Community Eco-Tourism", "Stay in authentic village homestays and community-operated eco-lodges."),
            ("Pristine Nature Walk", "Hike through lush oak forests alive with bird calls and waterfalls.")
        ],
        "itinerary": [
            {"title": "Drive Pokhara to Milan Chok, Trek to Ghale Kharka", "alt": "1,670m", "time": "1 hr drive + 4.5 hrs walk", "desc": "Ascend through Brahmin and Gurung farming hillsides with mountain views."},
            {"title": "Ghale Kharka to Tara Hilltop to Parche", "alt": "1,980m", "time": "5.5 hrs", "desc": "Trek through dense rhododendron forest up to Tara Hilltop for mountain views."},
            {"title": "Parche to Sikles Village & Exploration", "alt": "2,000m", "time": "2 hrs walk + village tour", "desc": "Short walk into Sikles village. Visit the Gurung museum, local school, and weavers."},
            {"title": "Sikles to Chipli / Kharka, Drive to Pokhara", "alt": "820m", "time": "3.5 hrs walk + 2 hrs drive", "desc": "Descend to the Modi river valley and private 4WD return to Pokhara."}
        ],
        "faqs": [
            ("What makes Sikles unique?", "Sikles has maintained its traditional architecture and Gurung customs with virtually zero tourist crowds.")
        ]
    },

    # --- 6. CULTURAL & PILGRIMAGE TREKS ---
    {
        "slug": "jomsom-muktinath-trek-with-poon-hill",
        "title": "Jomsom Muktinath Trek with Poon Hill",
        "category": "Cultural & Pilgrimage",
        "duration": "10-12 Days",
        "elevation": "3,800m (Muktinath Temple)",
        "grade": "Moderate",
        "price": "950",
        "image": "https://images.unsplash.com/photo-1516483638261-f4dbaf036963?auto=format&fit=crop&w=1200&q=80",
        "headline": "A grand pilgrimage through the deepest canyon on earth to the sacred 108 waterspouts of Muktinath.",
        "lead": "Combining the sunrise of Poon Hill with the ancient sacred temple of Muktinath, this classic journey travels through the deepest river gorge in the world: the Kali Gandaki.",
        "overview": "Witness sunrise from Poon Hill (3,210m), soak in natural hot springs at Tatopani, walk through the world's deepest gorge between Annapurna (8,091m) and Dhaulagiri (8,167m), sample apple cider in Marpha, and reach Muktinath (3,800m)—a holy sanctuary revered for centuries by Hindus and Buddhists.",
        "highlights": [
            ("Sacred Muktinath Temple (3,800m)", "Bathe in the 108 sacred water spouts and witness the eternal natural gas flame."),
            ("Poon Hill Sunrise (3,210m)", "Iconic dawn views over the Dhaulagiri and Annapurna ranges."),
            ("Kali Gandaki Gorge", "Hike through the deepest river gorge on planet Earth."),
            ("Apple Capital of Marpha", "Stroll through whitewashed Thakali alleys famous for apple orchards and brandies.")
        ],
        "itinerary": [
            {"title": "Drive Pokhara to Nayapul, Trek to Tikhedhunga", "alt": "1,540m", "time": "5.0 hrs", "desc": "Start the journey into the lower Annapurna valleys."},
            {"title": "Tikhedhunga to Ghorepani", "alt": "2,860m", "time": "5.5 hrs", "desc": "Climb Ulleri stone staircase into the rhododendron forests of Ghorepani."},
            {"title": "Poon Hill Sunrise (3,210m), Trek to Tatopani", "alt": "1,190m", "time": "6.5 hrs", "desc": "Poon Hill sunrise. Descend steeply down into the Kali Gandaki valley to the natural hot springs of Tatopani."},
            {"title": "Tatopani to Ghasa", "alt": "2,010m", "time": "5.5 hrs", "desc": "Walk through the narrowest section of the Kali Gandaki gorge between Annapurna and Dhaulagiri."},
            {"title": "Ghasa to Marpha", "alt": "2,670m", "time": "6.0 hrs", "desc": "Enter the Thakali homeland. Explore the whitewashed stone town of Marpha and apple orchards."},
            {"title": "Marpha to Kagbeni", "alt": "2,810m", "time": "4.5 hrs", "desc": "Walk along the windy riverbed to the gateway of Upper Mustang at Kagbeni."},
            {"title": "Kagbeni to Muktinath Temple", "alt": "3,800m", "time": "4.5 hrs", "desc": "Climb into the high Mustang desert to the holy pilgrimage shrine of Muktinath."},
            {"title": "Muktinath to Jomsom, Flight to Pokhara", "alt": "820m", "time": "Transit", "desc": "Morning temple visit, transfer to Jomsom airport for mountain flight to Pokhara."}
        ],
        "faqs": [
            ("Why is Muktinath sacred?", "Muktinath is one of the most sacred pilgrimage sites in South Asia, revered by Hindus as 'Mukti Kshetra' (place of liberation) and by Buddhists as Chumig Gyatsa."),
            ("How do we return to Pokhara?", "A scenic 20-minute flight from Jomsom to Pokhara provides aerial views of the mountains you just hiked through.")
        ]
    },

    # --- 7. MOUNTAIN VIEW / SCENIC TREKS ---
    {
        "slug": "annapurna-view-trek",
        "title": "Annapurna View Trek",
        "category": "Mountain View & Scenic",
        "duration": "5-6 Days",
        "elevation": "3,210m (Poon Hill Viewpoint)",
        "grade": "Easy-Moderate",
        "price": "520",
        "image": "https://images.unsplash.com/photo-1544735716-392fe2489ffa?auto=format&fit=crop&w=1200&q=80",
        "headline": "A curated scenic journey connecting the premier mountain viewpoints around the Annapurna Range.",
        "lead": "The Annapurna View Trek links together the finest panoramic viewpoints in western Nepal—Australian Camp, Sarangkot, Ghorepani, and Poon Hill—for non-stop Himalayan photography.",
        "overview": "Curated specifically for landscape photographers and mountain lovers, this trek avoids harsh extremes while keeping you stationed at premium sunrise and sunset viewpoints facing Machhapuchhre, Dhaulagiri, and Annapurna.",
        "highlights": [
            ("Multiple Premier Viewpoints", "Poon Hill, Australian Camp, and Sarangkot in one seamless itinerary."),
            ("Golden Hour Himalayan Photography", "Positioned for spectacular morning and evening alpenglow on 8,000m peaks."),
            ("Comfortable Heritage Lodging", "Hand-selected scenic lodges with panoramic mountain-view balconies."),
            ("Gentle Pacing", "Leisurely daily stages with generous photo stops.")
        ],
        "itinerary": [
            {"title": "Drive Pokhara to Phedi, Trek to Australian Camp", "alt": "2,060m", "time": "1 hr drive + 3 hrs walk", "desc": "Climb through Dhampus to Australian Camp for sunset over Fishtail Mountain."},
            {"title": "Australian Camp to Landruk", "alt": "1,565m", "time": "5.0 hrs", "desc": "Walk along forested ridges with views across the Modi river valley."},
            {"title": "Landruk to Tadapani", "alt": "2,630m", "time": "5.5 hrs", "desc": "Cross the river valley and climb through rhododendron forests to Tadapani."},
            {"title": "Tadapani to Ghorepani", "alt": "2,860m", "time": "5.0 hrs", "desc": "Scenic ridge walk with mountain views on both sides."},
            {"title": "Poon Hill Sunrise (3,210m), Descend & Drive to Pokhara", "alt": "820m", "time": "4 hrs walk + 2 hrs drive", "desc": "Unrivaled dawn views from Poon Hill, descend to roadhead, private jeep to Pokhara."}
        ],
        "faqs": [
            ("Is this good for photography?", "Yes, this itinerary is optimized around optimal dawn and dusk lighting on the snow peaks.")
        ]
    }
]

# Generate each trek page
ROOT_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
output_dir = os.path.join(ROOT_DIR, "treks")
os.makedirs(output_dir, exist_ok=True)

for trek in treks_data:
    filename = f"{trek['slug']}.html"
    filepath = os.path.join(output_dir, filename)
    content = generate_trek_page(trek)
    with open(filepath, "w", encoding="utf-8") as f:
        f.write(content)
    print(f"Generated: {filepath}")

print("All 14 requested trek pages successfully generated.")
