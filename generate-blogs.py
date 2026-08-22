#!/usr/bin/env python3
"""Generate 111 SEO blog posts for The Nail Ladie - Depoe Bay, Oregon."""
import os, textwrap, random

OUT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "blog")
os.makedirs(OUT, exist_ok=True)

SITE = {
    "name": "The Nail Ladie",
    "addr": "531 US-101 Suites K1-2, Depoe Bay, OR 97341",
    "phone": "(541) 992-1887",
    "book": "https://www.vagaro.com/thenailladie",
    "ig": "https://www.instagram.com/the_nail_ladie/",
    "fb": "https://www.facebook.com/thenailladie",
    "base": "https://luckygoats33.github.io/coastal-creations-salon",
    "logo": "https://d8j0ntlcm91z4.cloudfront.net/user_3681BqEuWywySamoBS6St7ib1O7/hf_20260722_034833_b9e47356-4e68-4480-8c47-b789a8988ac9.png",
}

# ─── 111 TOPICS ───────────────────────────────────────────────────────────────
TOPICS = [
    # 1-15: Service-specific (nails)
    ("Best Gel Manicure in Depoe Bay, Oregon", "gel-manicure-depoe-bay-oregon",
     "Discover why The Nail Ladie offers the best gel manicure on the Oregon Coast. Long-lasting, chip-free gel nails in Depoe Bay.",
     "gel manicure", "nails",
     ["Looking for a gel manicure that actually lasts? At The Nail Ladie in Depoe Bay, Oregon, Heather brings over 18 years of experience to every gel polish application. Whether you want a classic nude, a bold statement color, or something with a little sparkle, a gel manicure at our private studio salon is an experience you won't forget.",
      "A gel-polish manicure at The Nail Ladie starts at just $35 and includes meticulous nail prep, cuticle care, and a flawless two-coat gel application cured under LED light. The result? Nails that stay glossy and chip-free for two to three weeks — perfect for Oregon Coast living where your hands are always on display.",
      "What sets our gel manicures apart is the one-on-one attention. You're the only client in the salon during your appointment. No rushed service, no background noise — just Heather's expert hands and your favorite playlist. It's the kind of personalized care that keeps clients driving from Lincoln City, Newport, and even Portland.",
      "We use professional-grade gel polish systems that are gentle on your natural nails while delivering salon-quality shine. If you're switching from regular polish, you'll notice the difference immediately: no smudging, no drying time, and a mirror-like finish that turns heads.",
      "Ready to experience the best gel manicure on the Central Oregon Coast? Book your appointment online at vagaro.com/thenailladie or call us at (541) 992-1887. Walk-ins are welcome when availability allows, but we recommend booking ahead — Heather's schedule fills up fast."]),

    ("Dip Powder Nails: What to Expect at The Nail Ladie", "dip-powder-nails-depoe-bay",
     "Everything you need to know about dip powder nails at The Nail Ladie in Depoe Bay, Oregon. Durable, beautiful, no UV light required.",
     "dip powder nails", "nails",
     ["Dip powder nails have taken the beauty world by storm, and at The Nail Ladie in Depoe Bay, Oregon, we've perfected the technique. Our Gel & Powder Manicure ($65) combines the strength of dip powder with the smooth finish of gel for nails that last three to four weeks without chipping.",
      "So what exactly are dip powder nails? Instead of painting on polish, your nails are dipped into a fine, pigmented powder and sealed with a clear protective coat. The result is a thicker, more durable manicure than traditional gel — ideal for anyone who's hard on their hands.",
      "One of the biggest advantages of dip powder is that it doesn't require UV or LED curing. This makes it a great option for clients who prefer to avoid UV exposure. The powder also contains vitamins and calcium that can actually strengthen your natural nails over time.",
      "At The Nail Ladie, Heather offers a wide range of dip powder colors, from classic French tips to trendy earth tones and bold metallics. She'll help you choose the perfect shade and shape for your lifestyle. Plus, our intimate one-chair salon means you get her full attention from start to finish.",
      "Curious about dip powder nails? Book your appointment at The Nail Ladie — located at 531 US-101 Suites K1-2 in Depoe Bay. Call (541) 992-1887 or visit vagaro.com/thenailladie to reserve your spot."]),

    ("Gel-X Nail Extensions in Depoe Bay", "gel-x-nail-extensions-depoe-bay",
     "Full set of Gel-X nail extensions at The Nail Ladie in Depoe Bay, Oregon. Custom lengths, shapes, and designs starting at $110.",
     "gel-x nail extensions", "nails",
     ["Want longer nails without the damage? Gel-X nail extensions at The Nail Ladie in Depoe Bay are the answer. Starting at $110 for a full set, Gel-X tips are pre-shaped soft gel extensions that are bonded to your natural nail — no drilling, no harsh chemicals, no damage.",
      "Unlike traditional acrylic, Gel-X extensions are lightweight, flexible, and feel natural on your hands. They're applied using a special adhesive gel and cured under LED light, creating a seamless bond that lasts three to four weeks. Heather custom-fits each tip to your nail bed for a perfect, salon-quality look.",
      "At The Nail Ladie, you can choose from multiple lengths: Level 1 (active/short), Level 2 (medium, +$5), Level 3 (long, +$20), or Level 4 (extra-long, +$35). We also offer specialty shapes like coffin, stiletto, and almond — upgrades are just $15.",
      "Gel-X is the perfect base for nail art, too. Add simple designs (Tier 1, $15), medium art (Tier 2, $25), advanced designs (Tier 3, $50), or go all-out with custom nail art (Tier 4, $60). From hand-painted florals to chrome finishes, Heather can bring any design to life.",
      "Ready for your Gel-X transformation? The Nail Ladie is located at 531 US-101 in Depoe Bay, Oregon. Book online at vagaro.com/thenailladie or call (541) 992-1887."]),

    ("Nail Stamping Art: The Nail Ladie's Specialty", "nail-stamping-art-oregon-coast",
     "Discover nail stamping art at The Nail Ladie in Depoe Bay, Oregon. Intricate designs, custom patterns, and one-of-a-kind nail art on the Oregon Coast.",
     "nail stamping", "nails",
     ["Nail stamping is one of the most exciting techniques in modern nail art, and at The Nail Ladie in Depoe Bay, Oregon, it's one of our signature specialties. Using precision-engraved stamping plates and specialty polishes, Heather creates intricate designs that would be impossible to paint freehand.",
      "How does nail stamping work? A design is etched into a metal plate, filled with a special stamping polish, and then transferred to a silicone stamper. The stamper picks up the design perfectly and presses it onto your nail in one smooth motion. The result is a crisp, detailed pattern — from delicate lace to bold geometric shapes.",
      "At The Nail Ladie, stamping is available as part of our tiered nail art add-ons. Simple stamping designs start at $15 (Tier 1), while more complex multi-layer stamped looks fall into our Medium (Tier 2, $25) or Advanced (Tier 3, $50) categories. Want a fully custom stamped design? Our Tier 4 custom art ($60) lets you dream it up and Heather will make it happen.",
      "Stamping is incredibly versatile. It works on gel, dip powder, and regular polish. Popular stamping designs at our salon include ocean waves (perfect for the coastal vibe!), florals, mandalas, animal prints, and seasonal holiday patterns. You can also combine stamping with chrome, foils, or glitter for truly unique nails.",
      "Experience nail stamping artistry at The Nail Ladie. Our private salon is located at 531 US-101 in Depoe Bay. Book at vagaro.com/thenailladie or call (541) 992-1887 — and follow @the_nail_ladie on Instagram for stamping inspiration."]),

    ("Chrome Nails on the Oregon Coast", "chrome-nails-oregon-coast",
     "Mirror-finish chrome nails at The Nail Ladie in Depoe Bay. Rose gold, silver, holographic chrome — stunning nail art on the Oregon Coast.",
     "chrome nails", "nails",
     ["Chrome nails are the ultimate statement manicure, and nobody does them better on the Oregon Coast than The Nail Ladie in Depoe Bay. That mirror-like, metallic finish catches the light like liquid metal — and it's one of Heather's most requested services.",
      "Chrome nail art uses an ultra-fine metallic powder that's buffed onto a cured gel base coat. The powder particles create a seamless mirror effect that can range from classic silver to rose gold, champagne, blue chrome, or even holographic rainbow. The finish is so reflective you can literally see yourself in your nails.",
      "At The Nail Ladie, chrome and cat eye finishes are available as an add-on to any base manicure service. The results are stunning on any nail shape — from sleek almond to dramatic coffin. Chrome looks especially gorgeous paired with our structured gel or Gel-X extensions for that extra bit of length and drama.",
      "Chrome nails are also incredibly durable. The powder bonds to the gel surface and is sealed under a top coat, so your mirror finish stays flawless for the life of your manicure. No peeling, no fading — just pure, head-turning shine.",
      "Ready for chrome? Book your appointment at The Nail Ladie, 531 US-101 in Depoe Bay, Oregon. Visit vagaro.com/thenailladie or call (541) 992-1887."]),

    ("Cat Eye Nails: Magnetic Nail Art in Depoe Bay", "cat-eye-nails-depoe-bay",
     "Mesmerizing cat eye nails at The Nail Ladie in Depoe Bay, Oregon. Magnetic gel creates a shifting light effect that's truly one-of-a-kind.",
     "cat eye nails", "nails",
     ["Cat eye nails are pure magic — a shifting, three-dimensional light effect created with magnetic gel polish. At The Nail Ladie in Depoe Bay, Oregon, Heather has mastered this technique and it's become one of our most popular nail art styles.",
      "The cat eye effect is created using a special gel polish containing tiny metallic particles. When a magnet is held near the wet polish, the particles align to create a mesmerizing stripe of light that moves as you tilt your hand. The result looks like a cat's eye gemstone — hence the name.",
      "Cat eye gel comes in dozens of stunning colors. At The Nail Ladie, our most requested shades include deep emerald green, midnight blue, burgundy, champagne gold, and the ever-popular black cat eye. Each color creates a unique effect, and Heather can customize the light pattern — from a single bold stripe to a more diffused, galaxy-like glow.",
      "Cat eye is available as an add-on to any gel manicure, structured gel, or Gel-X extension service. It pairs beautifully with both short natural nails and longer extensions. Some clients even mix cat eye nails with chrome or glitter accent nails for a truly custom look.",
      "Experience the magic of cat eye nails at The Nail Ladie. Book online at vagaro.com/thenailladie or call (541) 992-1887. Our private salon is located at 531 US-101 in Depoe Bay, Oregon."]),

    ("Structured Gel Manicure: Strength Without Extensions", "structured-gel-manicure-depoe-bay",
     "Structured gel manicure at The Nail Ladie in Depoe Bay. Adds strength and thickness to natural nails without extensions. $65.",
     "structured gel manicure", "nails",
     ["Not ready for nail extensions but want something stronger than regular gel polish? A structured gel manicure at The Nail Ladie in Depoe Bay ($65) is the perfect middle ground. It adds a layer of builder gel over your natural nails for extra strength, thickness, and a gorgeous, even surface.",
      "Structured gel (also called builder gel or hard gel overlay) is a thicker gel product that's sculpted onto your natural nail and cured under LED light. Unlike regular gel polish, which is purely cosmetic, structured gel actually reinforces your nails — preventing breaks, chips, and peeling.",
      "This service is ideal for clients who want to grow their natural nails longer but struggle with breakage. The builder gel acts like a protective shield, allowing your nails to grow underneath while staying protected. It's also perfect for anyone with thin, weak, or damaged nails who wants them to look and feel healthier.",
      "At The Nail Ladie, Heather applies structured gel with precision, creating a smooth, even surface that looks naturally flawless. You can wear it clear for a natural look, or add any gel polish color on top. It's also the perfect base for nail art, chrome, or cat eye finishes.",
      "Book your structured gel manicure at The Nail Ladie — 531 US-101, Depoe Bay. Visit vagaro.com/thenailladie or call (541) 992-1887."]),

    ("Hard Gel Nail Extensions vs Gel-X: Which Is Right for You?", "hard-gel-vs-gel-x-extensions",
     "Comparing hard gel sculpted extensions and Gel-X tips at The Nail Ladie in Depoe Bay. Both $110 — here's how to choose.",
     "hard gel extensions", "nails",
     ["At The Nail Ladie in Depoe Bay, Oregon, we offer two premium nail extension options: sculpted hard gel extensions and Gel-X full-cover tips. Both start at $110 for a full set, but they use different techniques and offer different benefits. Here's how to choose.",
      "Sculpted hard gel extensions are built from scratch directly on your natural nail using a form and hard gel product. Heather hand-sculpts each nail to your desired length and shape, then cures it under LED light. The result is a completely custom extension that fits your nail bed perfectly. Sculpted nails tend to be slightly thinner and more natural-looking.",
      "Gel-X extensions use pre-made soft gel tips that are bonded to your natural nail with adhesive gel. The tips come in various shapes and sizes, and Heather selects the best fit for each finger. Gel-X is generally a faster application process and is easier to remove than hard gel.",
      "Both options are durable and long-lasting (3-4 weeks between fills). Hard gel is slightly more rigid and strong, making it better for clients who are very hard on their hands. Gel-X is lighter and more flexible, which some clients find more comfortable. Both can be customized with any nail art, chrome, or stamping design.",
      "Not sure which is right for you? Book a consultation at The Nail Ladie. Heather will assess your natural nails and lifestyle to recommend the best option. Visit vagaro.com/thenailladie or call (541) 992-1887."]),

    ("Nail Fill Schedule: When to Come Back", "nail-fill-schedule-guide",
     "How often should you get a nail fill? The Nail Ladie in Depoe Bay explains the ideal fill schedule for gel and extension nails.",
     "nail fill schedule", "nails",
     ["One of the most common questions we get at The Nail Ladie is: how often should I get a nail fill? The answer depends on your nail growth rate and the type of enhancement you're wearing. Here's our guide to the ideal fill schedule.",
      "For most clients, a 2-3 week fill is ideal. At The Nail Ladie, a standard nail fill at 2-3 weeks is $70. This is the sweet spot — there's enough new growth to see the gap, but not so much that the balance of the nail is affected. A fill at this stage is straightforward and keeps your nails looking fresh.",
      "If you wait 3-4 weeks, you'll need a fill and rebalance ($75). At this point, the weight distribution of the extension has shifted as your nail grows, so Heather will reshape and rebalance the product to maintain proper structure. This prevents lifting and breakage.",
      "Waiting 5-6 weeks between fills ($90) requires more extensive work. The gap is significant, and the nail may need additional product to fill the exposed area. We strongly recommend not going beyond 6 weeks, as the risk of lifting, moisture trapping, and breakage increases significantly.",
      "Pro tip: set up a recurring appointment every 2-3 weeks for the best results and lowest cost per visit. Book your fill schedule at vagaro.com/thenailladie or call The Nail Ladie at (541) 992-1887."]),

    ("Classic Pedicure on the Oregon Coast", "classic-pedicure-depoe-bay-oregon",
     "Treat your feet to a classic pedicure at The Nail Ladie in Depoe Bay, Oregon. Full spa pedicure from $70 on the Oregon Coast.",
     "pedicure", "pedicures",
     ["Your feet deserve some love too — especially after a day exploring the Oregon Coast. At The Nail Ladie in Depoe Bay, our classic pedicure ($70) is a full spa experience for your feet, complete with soaking, exfoliation, callus care, moisturizing massage, and a flawless polish application.",
      "Our classic pedicure starts with a warm soak to soften the skin and relax tired muscles. Next, Heather performs gentle callus removal and cuticle care to smooth rough spots and prep your nails. A hydrating sugar scrub exfoliates dead skin, followed by a luxurious foot and lower leg massage.",
      "Want the lasting power of gel on your toes? Upgrade to a Classic Pedicure with Gel Polish for $85. Gel pedicure polish lasts 3-4 weeks without chipping — perfect for sandal season on the beach. We also offer a Petite Pedicure ($35) for a quicker refresh, or add gel polish to the petite for $60.",
      "For extra relaxation, add our Hot Stone Massage upgrade ($15) to any classic pedicure. The warm basalt stones melt tension in your feet and calves — pure bliss after a long hike at Boiler Bay or a morning of whale watching.",
      "Treat yourself to a pedicure at The Nail Ladie in Depoe Bay. Book at vagaro.com/thenailladie or call (541) 992-1887."]),

    # 11-15: Service-specific (lashes)
    ("Classic Lash Extensions in Depoe Bay, Oregon", "classic-lash-extensions-depoe-bay",
     "Classic eyelash extensions at The Nail Ladie in Depoe Bay. Natural-looking lash enhancement starting at $150. Oregon Coast lash studio.",
     "classic lash extensions", "lashes",
     ["Classic lash extensions are the most natural-looking lash enhancement available, and at The Nail Ladie in Depoe Bay, Oregon, Heather applies them with precision and artistry. A full set of classic, hybrid, or volume lashes starts at just $150.",
      "Classic lash extensions involve applying a single synthetic lash to each of your natural lashes, one by one. The result is a subtle, mascara-like enhancement that adds length and definition without looking overdone. It's the perfect choice for first-time lash clients or anyone who prefers an understated, elegant look.",
      "At The Nail Ladie, we also offer hybrid lashes (a mix of classic and volume fans) and full volume lashes — all included in the same $150 full set price. Heather will consult with you before application to determine the best style, length, and curl for your eye shape and desired look.",
      "For clients who want maximum drama, our Mega Volume Fullset ($175) uses ultra-fine extensions in larger handmade fans for incredible density and fullness while keeping the weight comfortable on your natural lashes. It's the boldest lash look we offer.",
      "Lash fills keep your extensions looking full as your natural lashes shed. A 2-week fill is $75, 3-week fill is $85, and 4-week fill is $125. We recommend filling every 2-3 weeks for optimal fullness. Book at vagaro.com/thenailladie or call (541) 992-1887."]),

    ("Volume Lash Extensions: Full, Dramatic Lashes", "volume-lash-extensions-oregon-coast",
     "Volume and mega volume eyelash extensions at The Nail Ladie in Depoe Bay. Full, dramatic lashes on the Oregon Coast.",
     "volume lash extensions", "lashes",
     ["Volume lash extensions deliver the full, dramatic look that classic lashes can't achieve. At The Nail Ladie in Depoe Bay, Oregon, volume lashes are included in our $150 full set, while mega volume — for the most dramatic look — is $175.",
      "Volume lashes use multiple ultra-fine extensions fanned out and applied to a single natural lash. These handmade fans create incredible fullness and dimension while remaining surprisingly lightweight. The result is lashes that look impossibly thick and fluffy without weighing down your natural lashes.",
      "Mega Volume takes it even further. Using even finer extensions in larger fans, mega volume creates maximum density and drama. It's the go-to choice for special occasions, photoshoots, or anyone who simply loves bold, statement lashes.",
      "Heather is certified in both volume and mega volume techniques and customizes every set to complement your eye shape. Whether you prefer a natural fan for everyday wear or a dramatic cat-eye style for special events, she'll design the perfect set for you.",
      "Volume lash fills at The Nail Ladie are: 2-week fill $85, 3-week fill $125, and 4-week fill $150 for mega volume. Book your lash appointment at vagaro.com/thenailladie or call (541) 992-1887."]),

    ("Lash Lift and Tint: Low-Maintenance Lash Enhancement", "lash-lift-tint-depoe-bay",
     "Lash lift and tint at The Nail Ladie in Depoe Bay. Curled, darkened natural lashes with zero maintenance. Perfect for Oregon Coast living.",
     "lash lift and tint", "lashes",
     ["Not ready for full lash extensions? A lash lift and tint gives you beautifully curled, darkened natural lashes with absolutely zero daily maintenance. At The Nail Ladie in Depoe Bay, it's one of our most popular services for active, outdoor-loving Oregon Coast women.",
      "A lash lift is essentially a perm for your eyelashes. Using a silicone shield and a gentle lifting solution, Heather curls your natural lashes from the root, creating a wide-eyed, lifted look that lasts 6-8 weeks. The tint adds a semi-permanent dye that darkens your lashes, eliminating the need for mascara.",
      "The entire process takes about 45 minutes to an hour, and the results are immediate. You'll walk out with lashes that look longer, fuller, and more defined — without any extensions, adhesive, or daily upkeep. It's the ultimate low-maintenance beauty treatment.",
      "Lash lifts are perfect for anyone who wants to wake up looking put-together without spending time on makeup. They're also great for active lifestyles — swimming, surfing, hiking, whale watching — your lashes stay perfectly curled through it all.",
      "Book your lash lift and tint at The Nail Ladie in Depoe Bay. Visit vagaro.com/thenailladie or call (541) 992-1887."]),

    ("Eyelash Extension Aftercare Guide", "lash-extension-aftercare-guide",
     "How to care for your eyelash extensions. Complete aftercare guide from The Nail Ladie in Depoe Bay, Oregon.",
     "lash extension aftercare", "lashes",
     ["You just got a gorgeous new set of lash extensions at The Nail Ladie — now here's how to make them last. Proper aftercare is the key to keeping your lashes looking full and beautiful between fills. Follow these tips from Heather for the best results.",
      "The first 24-48 hours are critical. Avoid getting your lashes wet, steamy, or oily during this time. The adhesive needs time to fully cure. Skip the sauna, hot yoga, swimming, and heavy workouts for the first two days. When you do wash your face, avoid the eye area and pat dry gently.",
      "After the curing period, you can resume normal activities — but some habits will help your lashes last longer. Use oil-free makeup removers and cleansers around your eyes. Oil breaks down lash adhesive faster than anything else. We recommend a gentle, oil-free lash cleanser (ask Heather for her recommendation).",
      "Brush your lashes daily with a clean spoolie wand. This keeps them separated, aligned, and looking fluffy. Avoid rubbing your eyes, sleeping face-down on your pillow, and using waterproof mascara (it requires oil-based remover). If you must use mascara, apply it only to the tips — never at the base near the adhesive bond.",
      "Most clients find that 2-week fills ($75 at The Nail Ladie) keep their lashes looking full and fresh. Don't wait too long between fills — if too many lashes have shed, you may need a new full set instead. Book your fill at vagaro.com/thenailladie or call (541) 992-1887."]),

    ("Lash Removal: Safe Professional Removal at The Nail Ladie", "professional-lash-removal-depoe-bay",
     "Professional lash extension removal at The Nail Ladie in Depoe Bay. Safe, gentle removal that protects your natural lashes. $35.",
     "lash removal", "lashes",
     ["Thinking about taking a break from lash extensions? Professional removal is the only safe way to go. At The Nail Ladie in Depoe Bay, professional lash removal is $35 and takes about 20-30 minutes.",
      "Never, ever try to remove lash extensions yourself. Pulling or picking at extensions can rip out your natural lashes, causing damage that takes months to recover from. The adhesive used for professional lash application requires a specialized remover to dissolve safely.",
      "At The Nail Ladie, Heather uses a professional-grade cream remover that gently dissolves the adhesive bond without touching your natural lashes. The process is painless and relaxing — you simply lie back while the remover does its work. Once dissolved, the extensions slide off easily.",
      "After removal, Heather will assess the condition of your natural lashes and recommend any conditioning treatments. Most clients are surprised at how healthy their natural lashes look after professional removal. If you're planning to take a break, a lash lift and tint is a great alternative to maintain a polished look.",
      "Book your lash removal at The Nail Ladie in Depoe Bay. Visit vagaro.com/thenailladie or call (541) 992-1887."]),

    # 16-25: Location-based
    ("Best Nail Salon in Depoe Bay, Oregon", "best-nail-salon-depoe-bay-oregon",
     "The Nail Ladie is Depoe Bay's premier nail salon. Private, one-on-one service with 18+ years of experience. Book your appointment today.",
     "nail salon Depoe Bay", "location",
     ["If you're searching for the best nail salon in Depoe Bay, Oregon, look no further than The Nail Ladie. Located at 531 US-101 Suites K1-2, our private studio salon offers a completely different experience from the typical nail salon — and our clients wouldn't have it any other way.",
      "What makes The Nail Ladie special? For starters, it's a one-chair salon. When you book an appointment with Heather, you're her only client. There's no waiting, no rushing, no assembly-line service. You get her full, undivided attention from the moment you walk in until your nails are picture-perfect.",
      "Heather brings over 18 years of professional nail artistry experience. She specializes in gel manicures, Gel-X and sculpted hard gel extensions, dip powder, nail stamping, chrome finishes, cat eye designs, and intricate custom nail art. She's also a certified lash technician offering classic, volume, and mega volume extensions, plus lash lifts and tints.",
      "The salon itself reflects the coastal charm of Depoe Bay — relaxing, intimate, and welcoming. It's a space where you can unwind, chat, and leave feeling pampered and beautiful. Our 5-star reviews speak for themselves: clients consistently praise the quality of work, the personalized service, and the relaxing atmosphere.",
      "The Nail Ladie is open Wednesday through Saturday, 8 AM to 6:45 PM. Book online at vagaro.com/thenailladie or call (541) 992-1887."]),

    ("Nail Salon Near Lincoln City, Oregon", "nail-salon-near-lincoln-city-oregon",
     "The Nail Ladie in Depoe Bay is just 15 minutes from Lincoln City. Premium gel nails, lash extensions, and nail art near Lincoln City, Oregon.",
     "nail salon Lincoln City", "location",
     ["Looking for a top-rated nail salon near Lincoln City, Oregon? The Nail Ladie in Depoe Bay is just a quick 15-minute drive south on Highway 101 — and it's worth every minute of the trip.",
      "While Lincoln City has several nail salons, The Nail Ladie offers something you won't find anywhere else on the Central Oregon Coast: a completely private, one-on-one salon experience. No walk-in chaos, no waiting, no rushing. Just you, Heather, and 18 years of nail artistry expertise.",
      "Our full service menu includes everything from $35 classic manicures to $110 Gel-X extensions, plus eyelash extensions, pedicures, haircuts, and custom nail art including stamping, chrome, and cat eye finishes. Prices are competitive with Lincoln City salons, but the quality and experience are unmatched.",
      "The drive from Lincoln City to Depoe Bay is one of the most beautiful stretches of Highway 101. You'll pass gorgeous ocean views, Fogarty Creek State Recreation Area, and the charming shops of Depoe Bay. Many Lincoln City clients make a day of it — nails at The Nail Ladie, lunch at a Depoe Bay restaurant, and a whale watching stop before heading home.",
      "Heading south from Lincoln City? The Nail Ladie is on the right side of Highway 101 as you enter Depoe Bay. Book at vagaro.com/thenailladie or call (541) 992-1887."]),

    ("Nail Salon Near Newport, Oregon", "nail-salon-near-newport-oregon",
     "The Nail Ladie in Depoe Bay is just 15 minutes north of Newport. Premium nail services and lash extensions near Newport, Oregon.",
     "nail salon Newport", "location",
     ["Newport residents — your new favorite nail salon is just 15 minutes up Highway 101 in Depoe Bay. The Nail Ladie offers premium gel manicures, nail extensions, custom nail art, eyelash extensions, and more in a private, one-on-one setting.",
      "Many of our most loyal clients drive from Newport for their appointments. Why? Because The Nail Ladie offers something that larger Newport salons can't: completely personalized, one-on-one service. When you book with Heather, you're her only client. The attention to detail and quality of work is exceptional.",
      "Our pricing is straightforward and competitive. Gel-polish manicures start at $35, structured gel manicures are $65, and full nail extensions start at $110. We offer four tiers of nail art from simple ($15) to custom ($60), plus chrome, cat eye, and stamping designs.",
      "The scenic drive from Newport to Depoe Bay along Highway 101 passes through Otter Rock and the Devil's Punchbowl area — gorgeous ocean views the whole way. Many clients combine their nail appointment with lunch at one of Depoe Bay's waterfront restaurants.",
      "From Newport, head north on Highway 101. The Nail Ladie is on the left just past the Depoe Bay Bridge. Book at vagaro.com/thenailladie or call (541) 992-1887."]),

    ("Oregon Coast Nail Salon: Why Locals Choose The Nail Ladie", "oregon-coast-nail-salon-locals-choice",
     "The Nail Ladie is the Oregon Coast's favorite private nail salon. Discover why locals from Depoe Bay to Newport choose us.",
     "Oregon Coast nail salon", "location",
     ["When it comes to nail care on the Oregon Coast, locals know where to go: The Nail Ladie in Depoe Bay. Since opening, Heather has built a loyal following of clients from across the Central Oregon Coast — Lincoln City, Newport, Otter Rock, Waldport, and beyond.",
      "What keeps Oregon Coast locals coming back? Three things: quality, consistency, and the one-on-one experience. In a big salon, you might get a different technician every visit. At The Nail Ladie, it's always Heather. She knows your nail history, your preferences, your go-to shapes and colors. That continuity makes a real difference.",
      "The Oregon Coast lifestyle demands durable nail services. Between ocean air, tide pool exploring, gardening, and outdoor adventures, your nails need to hold up. Heather's gel manicures, structured gel overlays, and extensions are built to last — not just look pretty in the parking lot.",
      "We're also proud to be part of the Depoe Bay community. The Nail Ladie isn't a chain or a franchise — it's Heather's dream realized. A small-town salon with big-city quality, right in the heart of the Whale Watching Capital of the Oregon Coast.",
      "Experience the local favorite. Book at vagaro.com/thenailladie or call (541) 992-1887. Located at 531 US-101 in Depoe Bay."]),

    ("Nail Salon on Highway 101 in Depoe Bay", "nail-salon-highway-101-depoe-bay",
     "Easy to find nail salon right on Highway 101 in Depoe Bay, Oregon. Free parking, walk-in friendly. The Nail Ladie.",
     "nail salon Highway 101", "location",
     ["Finding a great nail salon shouldn't require GPS gymnastics. The Nail Ladie is located right on Highway 101 in Depoe Bay, Oregon — at 531 US-101 Suites K1-2. You can't miss us, and there's free parking right out front.",
      "Whether you're driving up from Newport, down from Lincoln City, or passing through on an Oregon Coast road trip, The Nail Ladie is one of the easiest salons to find and access. Pull right in off Highway 101, park in front of the building, and walk in. No side streets, no confusing strip mall navigation.",
      "While we do recommend booking ahead (Heather works one-on-one and her schedule fills up fast), walk-ins are welcome when availability allows. Call ahead at (541) 992-1887 to check same-day openings, or book online anytime at vagaro.com/thenailladie.",
      "Our salon is part of the charming Depoe Bay commercial corridor on Highway 101. After your appointment, explore the world's smallest navigable harbor, watch for whales from the seawall, or grab fresh chowder at one of the nearby restaurants. Depoe Bay is a gem of the Oregon Coast.",
      "Open Wednesday through Saturday, 8 AM to 6:45 PM. The Nail Ladie — premium nails on Highway 101 in Depoe Bay."]),

    ("Central Oregon Coast Beauty Services", "central-oregon-coast-beauty-services",
     "Nails, lashes, hair, and makeup on the Central Oregon Coast. The Nail Ladie in Depoe Bay offers full beauty services.",
     "Central Oregon Coast beauty", "location",
     ["The Central Oregon Coast — from Lincoln City to Newport — is known for stunning natural beauty. Now there's a salon that matches: The Nail Ladie in Depoe Bay offers a full range of beauty services including nails, eyelash extensions, haircuts, pedicures, and Seint makeup artistry.",
      "For nails, our menu covers everything from a quick $15 nail trim to elaborate custom nail art and full Gel-X extensions. Gel-polish manicures, structured gel, dip powder, chrome finishes, cat eye nails, and stamping art — if you've seen it on Instagram, Heather can do it.",
      "Our lash services include classic, volume, and mega volume extensions, lash lifts and tints, and professional removal. Whether you want subtle enhancement or full-on drama, we've got you covered.",
      "We also offer haircuts ($35-$50), buzz cuts ($20), bang trims ($15), and blowouts ($15-$35). Plus, as a Seint Beauty artist, Heather provides custom color matching and makeup application — perfect for special events, wedding prep, or just learning your best everyday look.",
      "The Nail Ladie is centrally located in Depoe Bay at 531 US-101, easily accessible from anywhere on the Central Oregon Coast. Book at vagaro.com/thenailladie or call (541) 992-1887."]),

    ("Otter Rock to Depoe Bay: Quick Drive to The Nail Ladie", "otter-rock-nail-salon-depoe-bay",
     "Live in Otter Rock? The Nail Ladie in Depoe Bay is just 5 minutes away. Premium nail salon near Otter Rock, Oregon.",
     "nail salon Otter Rock", "location",
     ["If you're in Otter Rock, Oregon, the best nail salon on the coast is practically in your backyard. The Nail Ladie in Depoe Bay is just a 5-minute drive north on Highway 101 — closer than any salon in Newport or Lincoln City.",
      "Otter Rock is a quiet, beautiful community nestled between Newport and Depoe Bay. While it doesn't have its own nail salon, The Nail Ladie is so close that many Otter Rock residents consider it their local spot. Quick trip up 101, free parking out front, and you're in Heather's chair.",
      "We offer the full range of nail and beauty services that you'd find in a big-city salon, but with small-town charm and one-on-one attention. Gel manicures from $35, nail extensions from $110, lash extensions from $150, pedicures from $35, and haircuts from $35.",
      "After your appointment, Depoe Bay is the perfect spot for a quick lunch or a whale watching break before heading back to Otter Rock. The whole trip takes less time than driving to Newport — and the results are worth the short drive.",
      "Book your appointment at vagaro.com/thenailladie or call (541) 992-1887. The Nail Ladie, 531 US-101, Depoe Bay."]),

    ("Waldport and Yachats: Nail Services Worth the Drive", "waldport-yachats-nail-salon-depoe-bay",
     "Driving from Waldport or Yachats? The Nail Ladie in Depoe Bay offers premium nail and lash services worth the scenic Highway 101 trip.",
     "nail salon Waldport Yachats", "location",
     ["If you live in Waldport, Yachats, or the southern Central Oregon Coast, The Nail Ladie in Depoe Bay is worth the scenic drive up Highway 101. About 45 minutes from Waldport and an hour from Yachats, our private salon offers a level of service and artistry you won't find closer to home.",
      "The drive itself is one of the most beautiful stretches of the Oregon Coast — passing through Newport, Otter Rock, and along dramatic cliff-side ocean views. Many Waldport and Yachats clients make it a coastal day trip: nails at The Nail Ladie, lunch in Depoe Bay, and maybe a stop at the Newport Bayfront on the way home.",
      "Our services include everything from quick gel-polish manicures ($35) to full sets of sculpted nail extensions ($110), plus eyelash extensions ($150-$175), pedicures ($35-$85), and custom nail art. We offer a level of nail artistry — including stamping, chrome, and cat eye designs — that's rare outside of Portland.",
      "If you're making the drive, consider booking a combo appointment. Get your nails and lashes done in one visit, or treat yourself to a manicure and pedicure. Heather will work with you to schedule everything efficiently.",
      "Book at vagaro.com/thenailladie or call (541) 992-1887. The Nail Ladie, 531 US-101, Depoe Bay, Oregon."]),

    ("Tillamook to Depoe Bay: Nail Salon Worth the Trip", "tillamook-nail-salon-depoe-bay",
     "From Tillamook to Depoe Bay — The Nail Ladie is worth the 45-minute drive for premium nail art and lash extensions on the Oregon Coast.",
     "nail salon Tillamook", "location",
     ["Tillamook County residents looking for a premium nail experience — The Nail Ladie in Depoe Bay is about 45 minutes south on Highway 101, and our clients from Tillamook, Oceanside, and Pacific City say the drive is absolutely worth it.",
      "Why drive past other nail salons to get to The Nail Ladie? It comes down to artistry and experience. Heather specializes in custom nail art, stamping designs, chrome and cat eye finishes, and precision gel work that most salons simply don't offer. Plus, the private one-on-one salon experience is unlike anything you'll find in a traditional salon.",
      "The scenic drive from Tillamook to Depoe Bay takes you through some of Oregon's most beautiful coastal scenery. Pass through Pacific City, Neskowin, and Lincoln City before arriving in charming Depoe Bay. Make a day of it — cheese tasting in Tillamook, nails in Depoe Bay, and whale watching before heading home.",
      "We're open Wednesday through Saturday, 8 AM to 6:45 PM. With services ranging from $15 nail trims to $175 mega volume lash sets, there's something for every budget and style.",
      "Book your appointment at vagaro.com/thenailladie or call (541) 992-1887."]),

    # 26-35: Seasonal
    ("Summer Nails on the Oregon Coast", "summer-nails-oregon-coast",
     "Summer nail trends and beach-ready manicures at The Nail Ladie in Depoe Bay. Gel nails that survive sand, saltwater, and sunshine.",
     "summer nails", "seasonal",
     ["Summer on the Oregon Coast calls for nails that can keep up with your adventures. At The Nail Ladie in Depoe Bay, we specialize in durable, beach-ready manicures that look stunning whether you're tide pooling, kayaking, or enjoying a sunset dinner.",
      "Our gel-polish manicures ($35) and structured gel manicures ($65) are the top summer picks. Gel polish resists chips, peeling, and fading — even after swimming in the ocean or playing in the sand. Structured gel adds extra strength for active hands. Both last 2-3 weeks with zero maintenance.",
      "Hot summer nail trends for 2026 include ocean-inspired ombre (think sandy beige fading to deep teal), bright coral and turquoise solids, seashell and starfish stamping art, chrome in rose gold and holographic finishes, and neon French tips. Heather can create any of these looks — and much more.",
      "For your summer pedicure, our Classic Pedicure ($70) is the perfect treat for sandal-ready feet. Add gel polish ($85) for chip-free color that lasts through your entire beach vacation. Don't forget our Hot Stone Massage add-on ($15) — pure relaxation.",
      "Get your summer nails at The Nail Ladie, 531 US-101 in Depoe Bay. Book at vagaro.com/thenailladie or call (541) 992-1887."]),

    ("Holiday Nails: Festive Nail Art in Depoe Bay", "holiday-nails-festive-nail-art-depoe-bay",
     "Holiday nail art at The Nail Ladie in Depoe Bay, Oregon. Festive designs, glitter, red and gold, Christmas nail art on the Oregon Coast.",
     "holiday nails", "seasonal",
     ["The holidays are the perfect time to treat yourself to festive nail art, and The Nail Ladie in Depoe Bay is your go-to for stunning holiday designs. From elegant red and gold to playful snowflakes and reindeer, Heather creates holiday nail art that will be the star of every gathering.",
      "Our most popular holiday nail looks include classic red with gold foil accents, deep burgundy with champagne chrome, emerald green cat eye, snowflake and pine tree stamping designs, candy cane French tips, and glitter ombre in silver or gold. Each design is customized to your style and nail shape.",
      "Holiday nail art is available at all four tiers: Simple (Tier 1, $15) covers single-color accents and simple stamping. Medium (Tier 2, $25) includes two-color designs and detailed stamping. Advanced (Tier 3, $50) features multi-technique designs combining stamping, chrome, and hand-painted elements. Custom (Tier 4, $60) is your dream holiday nails — anything goes.",
      "Pro tip: book your holiday nail appointment early! December is our busiest month, and appointment slots fill up fast. Consider booking your holiday manicure in late November or early December to ensure you get the look you want for all your celebrations.",
      "Book your holiday nails at vagaro.com/thenailladie or call (541) 992-1887."]),

    ("Fall Nail Trends: Cozy Season Manicures", "fall-nail-trends-oregon-coast",
     "Fall nail trends at The Nail Ladie in Depoe Bay. Warm tones, earth colors, and cozy autumn nail art on the Oregon Coast.",
     "fall nails", "seasonal",
     ["Fall on the Oregon Coast is magical — stormy ocean views, cozy cafes, and the most beautiful color palette of the year. At The Nail Ladie in Depoe Bay, we embrace the season with warm-toned manicures that perfectly complement the autumn vibes.",
      "Trending fall nail colors include burnt orange, deep burgundy, forest green, chocolate brown, mustard yellow, warm nude, and rich plum. These earth tones look stunning on any skin tone and pair beautifully with fall fashion. For something more dramatic, try a dark cat eye in midnight blue or emerald.",
      "Fall nail art ideas include maple leaf stamping, cozy plaid patterns, tortoiseshell designs, gold foil accents, abstract marble in warm tones, and ombre in sunset colors. Heather can create any of these looks using stamping, freehand painting, or a combination of techniques.",
      "Fall is also the perfect time to try chrome nails. Champagne chrome, copper chrome, and rose gold chrome all complement the autumn color palette beautifully. Add chrome to any gel manicure or extension for a head-turning metallic finish.",
      "Cozy up with a fall manicure at The Nail Ladie. Book at vagaro.com/thenailladie or call (541) 992-1887."]),

    ("Spring Nail Designs: Fresh Looks for the Season", "spring-nail-designs-depoe-bay",
     "Spring nail designs at The Nail Ladie in Depoe Bay. Pastels, florals, and fresh spring manicures on the Oregon Coast.",
     "spring nails", "seasonal",
     ["Spring on the Oregon Coast brings blooming wildflowers, longer days, and the irresistible urge to refresh your look. At The Nail Ladie in Depoe Bay, our spring nail designs capture the season's energy with pastels, florals, and fresh, playful color combinations.",
      "Top spring nail trends include lavender, mint green, baby pink, periwinkle, coral, and butter yellow. These soft pastels look beautiful as solid colors, but they really come alive with spring-themed nail art — cherry blossom stamping, daisy accents, butterfly designs, and abstract watercolor effects.",
      "For the spring bride-to-be, we offer elegant bridal nail designs from simple French tips to delicate lace stamping and pearl accents. Our custom nail art (Tier 4, $60) allows for completely bespoke bridal designs — let Heather create nails that match your bouquet, your dress, or your wedding palette.",
      "Spring is also a great time to try our Gel-X extensions if you've been thinking about going longer. The soft gel tips are gentle on natural nails and provide the perfect canvas for spring nail art. A full set starts at $110, plus your choice of art.",
      "Welcome spring with fresh nails at The Nail Ladie. Book at vagaro.com/thenailladie or call (541) 992-1887."]),

    ("Winter Nail Care Tips for Oregon Coast Living", "winter-nail-care-tips-oregon-coast",
     "Winter nail care tips from The Nail Ladie in Depoe Bay. How to keep your nails strong and healthy through Oregon Coast winters.",
     "winter nail care", "seasonal",
     ["Oregon Coast winters are beautiful but brutal on your nails. The combination of cold wind, rain, indoor heating, and dry air can leave nails brittle, peeling, and prone to breakage. Here are Heather's top winter nail care tips from The Nail Ladie in Depoe Bay.",
      "Moisturize obsessively. Apply cuticle oil at least twice a day — morning and night. The dry, heated air inside your home pulls moisture from your nails and cuticles, leading to hangnails and brittle nails. Keep a cuticle oil pen in your purse for on-the-go application.",
      "Wear gloves — and not just for cold weather. Wear rubber gloves when washing dishes, cleaning, or doing any work with water and chemicals. Extended water exposure causes nails to expand and contract, leading to weakening and peeling. This is the number one cause of nail damage we see.",
      "Consider a structured gel overlay ($65 at The Nail Ladie) for added protection during winter. The builder gel acts as a shield over your natural nails, preventing breakage while your nails grow stronger underneath. It's like a winter coat for your nails.",
      "Book a winter nail care appointment at The Nail Ladie. Heather can assess your nails and recommend the best protection strategy. Visit vagaro.com/thenailladie or call (541) 992-1887."]),

    ("Valentine's Day Nails: Romantic Nail Art Ideas", "valentines-day-nails-depoe-bay",
     "Valentine's Day nail art at The Nail Ladie in Depoe Bay. Heart designs, red nails, pink ombre, and romantic nail looks.",
     "Valentine's Day nails", "seasonal",
     ["Valentine's Day is the perfect excuse for a romantic manicure, and at The Nail Ladie in Depoe Bay, Heather creates stunning Valentine's-themed nail art that's as unique as your love story.",
      "Classic Valentine's looks include all shades of red — from bright cherry to deep burgundy — with options for matte, glossy, or shimmer finishes. Pink ombre, from blush to magenta, is another romantic choice. For something bolder, try red chrome nails for a mirror-finish heart-stopper.",
      "Valentine's nail art at The Nail Ladie ranges from subtle to show-stopping. Simple heart stamping on an accent nail (Tier 1, $15) keeps it sweet. Heart outlines, love letter typography, and cupid arrow designs (Tier 2, $25) add more personality. For the full Valentine's experience, try multi-design custom art (Tier 3-4, $50-$60) with hearts, roses, and glitter.",
      "Don't forget: Valentine's Day is also a wonderful gift idea. Book a nail appointment for someone you love, or treat yourselves to a couples' nail day. Heather is happy to accommodate friends, couples, or mother-daughter appointments with back-to-back scheduling.",
      "Book your Valentine's nails at vagaro.com/thenailladie or call (541) 992-1887."]),

    ("4th of July Nail Art: Patriotic Designs in Depoe Bay", "fourth-of-july-nails-depoe-bay",
     "4th of July nail art at The Nail Ladie in Depoe Bay, Oregon. Red, white, and blue nail designs for Independence Day on the Oregon Coast.",
     "4th of July nails", "seasonal",
     ["Fourth of July on the Oregon Coast is a celebration — fireworks over the harbor, parades, barbecues, and beach bonfires. Complete your Independence Day look with patriotic nail art from The Nail Ladie in Depoe Bay.",
      "Our most popular 4th of July designs include red, white, and blue color blocking, American flag accent nails, star stamping patterns, firework burst designs, and red-and-blue glitter ombre. Heather can create anything from subtle patriotic accents to full-on, all-ten-fingers statement nails.",
      "For a modern twist on patriotic nails, try chrome in metallic red or blue, star-spangled cat eye nails, or abstract red and blue watercolor effects. These contemporary designs nod to the holiday without being too literal — perfect for those who want festive but sophisticated.",
      "Pro tip: book your 4th of July nails a week or two early. Our gel manicures last 2-3 weeks, so getting your nails done in late June means they'll be perfect for all your holiday celebrations. Plus, you avoid the last-minute rush.",
      "Get your 4th of July nails at The Nail Ladie. Book at vagaro.com/thenailladie or call (541) 992-1887."]),

    ("Halloween Nail Art: Spooky Season on the Coast", "halloween-nail-art-depoe-bay",
     "Halloween nail art at The Nail Ladie in Depoe Bay. Spooky, creepy, and cute Halloween nail designs on the Oregon Coast.",
     "Halloween nails", "seasonal",
     ["Spooky season meets coastal vibes at The Nail Ladie in Depoe Bay. Halloween is one of the most creative times of year for nail art, and Heather loves designing one-of-a-kind Halloween looks that range from cute to creepy to downright terrifying.",
      "Popular Halloween nail designs include jack-o'-lantern faces, spiderweb stamping, ghost and bat silhouettes, black cat designs (pair with actual cat eye gel for extra magic!), dripping blood tips, candy corn ombre, and Día de los Muertos sugar skull art.",
      "For an elegant Halloween look, try deep black with gold foil accents, dark purple cat eye, black chrome nails, or burgundy with cobweb stamping. These designs are sophisticated enough for everyday wear while still channeling spooky season energy.",
      "Halloween nail art is available at all four tiers. A simple orange-and-black accent (Tier 1, $15) is festive and fun. For more detail — like stamped spiderwebs or hand-painted ghosts — go with Tier 2 ($25) or Tier 3 ($50). Full custom Halloween designs (Tier 4, $60) let your imagination run wild.",
      "Book your Halloween nails at vagaro.com/thenailladie or call (541) 992-1887."]),

    ("Beach-Ready Nails for Your Oregon Coast Vacation", "beach-ready-nails-oregon-coast-vacation",
     "Planning an Oregon Coast vacation? Get beach-ready nails at The Nail Ladie in Depoe Bay. Durable, beautiful manicures that survive the beach.",
     "beach nails vacation", "seasonal",
     ["Planning an Oregon Coast vacation? Start it right with beach-ready nails from The Nail Ladie in Depoe Bay. Whether you're here for a weekend getaway or a week-long coastal retreat, our gel manicures are built to survive sand, saltwater, and all your seaside adventures.",
      "For the ultimate vacation nails, we recommend our gel-polish manicure ($35) or structured gel manicure ($65) for extra durability. Both resist chips, peeling, and fading — even after days of beach activities. Add a gel pedicure ($35) for picture-perfect toes in your sandals.",
      "Vacation-perfect nail designs include ocean-inspired ombre (sandy tan to seafoam), tropical colors like coral and turquoise, seashell and starfish stamping, mermaid chrome in iridescent green, and classic coastal neutrals. All of these look gorgeous in your vacation photos.",
      "Visiting from out of town? We love welcoming vacation guests. Book ahead online at vagaro.com/thenailladie to secure your spot — especially during peak summer season (June through September). Same-day availability is limited, so advance booking is strongly recommended.",
      "Get vacation-ready nails at The Nail Ladie, 531 US-101 in Depoe Bay. Call (541) 992-1887."]),

    ("New Year's Eve Nail Art: Ring in the New Year", "new-years-eve-nails-depoe-bay",
     "Celebrate New Year's Eve with glamorous nail art from The Nail Ladie in Depoe Bay. Glitter, chrome, and midnight glam nails.",
     "New Year's Eve nails", "seasonal",
     ["Ring in the new year with nails that sparkle as bright as the midnight countdown. At The Nail Ladie in Depoe Bay, our New Year's Eve nail designs bring the glamour, the glitter, and the drama.",
      "Top NYE nail trends include full glitter sets in gold, silver, or champagne, mirror chrome in any metallic shade, black and gold color blocking, holographic rainbow chrome, and midnight blue cat eye with silver foil accents. These are nails that catch the light — and every eye in the room.",
      "For the ultimate statement, try our custom nail art (Tier 4, $60) for a multi-technique design. Imagine black almond nails with gold chrome tips, champagne glitter ombre, and a clock-face accent nail showing midnight. That's the kind of wearable art Heather creates.",
      "Book your NYE nails by mid-December to guarantee your preferred appointment time. The last week of December books up quickly, and you'll want time to enjoy your festive nails at all your holiday parties.",
      "Celebrate in style. Book at vagaro.com/thenailladie or call (541) 992-1887."]),

    # 36-50: Educational
    ("How Long Do Gel Nails Last? Complete Guide", "how-long-do-gel-nails-last",
     "How long do gel nails last? Complete guide from The Nail Ladie in Depoe Bay covering gel polish, structured gel, and extensions.",
     "how long gel nails last", "educational",
     ["One of the most common questions we hear at The Nail Ladie: how long do gel nails actually last? The answer depends on the type of gel service you get and how you care for your nails. Here's the complete breakdown.",
      "Gel-polish manicures typically last 2-3 weeks without chipping. Some clients push it to 3-4 weeks, but by then you'll notice noticeable growth at the base. Gel polish doesn't grow with your nail, so the gap becomes visible. We recommend rebooking every 2-3 weeks for the best look.",
      "Structured gel manicures (builder gel overlay) last 3-4 weeks and can be filled rather than removed. The builder gel grows with your natural nail, and a fill appointment reshapes and adds product where needed. This makes structured gel more cost-effective over time.",
      "Gel-X and sculpted hard gel extensions last 3-4 weeks before needing a fill. With regular 2-3 week fills ($70), you can wear extensions indefinitely. The key is not waiting too long between fills — longer gaps mean more expensive fills and higher risk of lifting.",
      "To maximize gel nail longevity: avoid soaking your hands in water for extended periods, wear gloves when cleaning, apply cuticle oil daily, and avoid using your nails as tools. Follow these tips and your gel manicure will last its full lifespan. Questions? Ask Heather at your next appointment. Book at vagaro.com/thenailladie."]),

    ("Gel vs Dip Powder: Which Is Right for You?", "gel-vs-dip-powder-nails-comparison",
     "Gel vs dip powder nails — which is right for you? The Nail Ladie in Depoe Bay compares durability, look, removal, and cost.",
     "gel vs dip powder", "educational",
     ["Gel and dip powder are two of the most popular nail enhancement options, but they offer different benefits. At The Nail Ladie in Depoe Bay, we offer both and can help you choose the right one for your lifestyle. Here's a side-by-side comparison.",
      "Durability: Dip powder generally lasts slightly longer (3-4 weeks vs 2-3 for gel polish). However, structured gel and hard gel overlays match dip powder's durability. If chip-resistance is your top priority, both dip powder and structured gel are excellent choices.",
      "Finish and look: Gel polish offers the widest color range and the most natural, glossy finish. Dip powder tends to be slightly thicker and can look more opaque. If you prefer a thin, natural-looking manicure, gel is usually the better choice. If you want extra strength and don't mind a bit more thickness, dip powder wins.",
      "Removal: Gel polish is removed by soaking in acetone for 10-15 minutes. Dip powder also requires acetone soaking but typically takes a bit longer. Neither should ever be peeled off — that damages your natural nails. Removal at The Nail Ladie is $15 for gel, or included when rebooking.",
      "Health considerations: Dip powder contains vitamins and calcium that can strengthen nails. Gel requires UV/LED curing, though modern LED lamps use minimal UV exposure. Both are safe when applied and removed by a professional. Book either service at vagaro.com/thenailladie."]),

    ("Classic vs Volume Lash Extensions: A Complete Guide", "classic-vs-volume-lash-extensions-guide",
     "Classic vs volume lash extensions explained. The Nail Ladie in Depoe Bay breaks down the differences in look, weight, and maintenance.",
     "classic vs volume lashes", "educational",
     ["Choosing between classic and volume lash extensions? This guide from The Nail Ladie in Depoe Bay will help you decide which style is perfect for your eyes and lifestyle.",
      "Classic lashes apply one synthetic extension to each natural lash. The result is subtle, natural enhancement — like wearing perfect mascara all the time. Classic lashes add length and slight definition without dramatic fullness. They're ideal for first-time lash clients and anyone who prefers an understated look.",
      "Volume lashes use multiple ultra-fine extensions formed into a fan and applied to each natural lash. The result is noticeably fuller, fluffier, and more dramatic. Volume lashes fill in sparse areas and create density that classic lashes can't achieve. They're perfect for clients who want that 'wow' factor.",
      "At The Nail Ladie, both classic and volume lashes are included in our $150 full set price. We also offer hybrid lashes — a mix of both techniques — for clients who want something in between. Mega volume ($175) takes fullness to the maximum level.",
      "Maintenance is similar for both: 2-week fills to keep them looking full. Classic fills are slightly faster since there are fewer lashes to replace. Volume fills take a bit longer but maintain that luxurious fullness. Either way, Heather will have you looking amazing. Book at vagaro.com/thenailladie."]),

    ("Nail Shapes Guide: Find Your Perfect Shape", "nail-shapes-guide-choosing-best-shape",
     "Complete nail shapes guide from The Nail Ladie in Depoe Bay. Round, oval, square, almond, coffin, stiletto — find your perfect shape.",
     "nail shapes guide", "educational",
     ["Your nail shape can completely change the look of your manicure. At The Nail Ladie in Depoe Bay, Heather helps every client find the shape that best complements their hand shape, lifestyle, and personal style. Here's our guide to the most popular nail shapes.",
      "Round: The classic, low-maintenance shape. Round nails follow the natural curve of your fingertip and are filed into a gentle semicircle. Best for short nails and active lifestyles. This is included as a standard shape in all our services.",
      "Oval: Slightly more elongated than round, oval nails taper gently at the tip. They make fingers look longer and more slender. Oval is a timeless, elegant choice that works at any length. Also included as a standard shape.",
      "Square: Straight sides with a flat, squared-off tip. Square nails are bold and modern. They work best on longer nails but can look great short too. Squoval (square-oval) softens the corners slightly for a more versatile look. Both included as standard shapes.",
      "Almond, coffin, and stiletto are specialty shapes available as an upgrade ($15). Almond tapers to a soft point — elegant and feminine. Coffin (also called ballerina) is square-tipped with tapered sides — trendy and Instagram-worthy. Stiletto comes to a dramatic sharp point — bold and fierce. Ask Heather which specialty shape suits you best. Book at vagaro.com/thenailladie."]),

    ("How to Make Your Manicure Last Longer", "how-to-make-manicure-last-longer",
     "Pro tips to make your manicure last longer from The Nail Ladie in Depoe Bay. Extend the life of your gel, dip, or extension nails.",
     "make manicure last longer", "educational",
     ["Nothing's worse than a fresh manicure that chips after a few days. At The Nail Ladie in Depoe Bay, our gel manicures are built to last — but your habits at home make a huge difference too. Here are Heather's pro tips for maximum manicure longevity.",
      "Tip #1: Wear gloves for cleaning and dishes. This is the single most impactful thing you can do. Water exposure causes nails to expand and contract, weakening the bond between gel and your natural nail. Even 10 minutes of dishwashing without gloves can shorten your manicure's life by a week.",
      "Tip #2: Apply cuticle oil daily. Hydrated cuticles and nail beds keep the gel flexible and prevent lifting at the edges. Jojoba oil is the gold standard — its molecular structure is closest to your natural nail oil. A quick dab on each cuticle before bed works wonders.",
      "Tip #3: Don't use your nails as tools. Opening cans, peeling stickers, scratching surfaces — these motions stress the gel bond and can cause chips or lifting. Use actual tools instead. Your nails will thank you.",
      "Tip #4: Avoid acetone-based products. If you need to clean your hands with sanitizer or remove other products, use acetone-free options. Acetone breaks down gel polish. Follow these tips and your manicure from The Nail Ladie will go the distance. Book at vagaro.com/thenailladie."]),

    ("First Time Getting Gel Nails? What to Expect", "first-time-gel-nails-what-to-expect",
     "First time getting gel nails? Here's exactly what to expect at your appointment at The Nail Ladie in Depoe Bay, Oregon.",
     "first time gel nails", "educational",
     ["Getting gel nails for the first time? We love first-time clients at The Nail Ladie in Depoe Bay, and Heather will make sure your experience is comfortable, relaxing, and exciting. Here's exactly what to expect at your first gel nail appointment.",
      "When you arrive at our private salon at 531 US-101 in Depoe Bay, it's just you and Heather. She'll start with a consultation: what look are you going for? What's your daily routine? What's your nail history? This helps her recommend the best service — gel polish ($35) for a simple upgrade, structured gel ($65) for added strength, or extensions ($110) for added length.",
      "Next comes nail prep. Heather gently pushes back your cuticles, shapes your nails to your desired shape (round, oval, square, or squoval are standard), and lightly buffs the nail surface. This creates the perfect base for gel adhesion. Don't worry — it's painless and quick.",
      "Then the fun part: color selection! Heather has an extensive color collection and will help you choose the perfect shade. The gel is applied in thin layers, each cured under an LED lamp for 30-60 seconds. The curing process feels warm but never painful. Most gel manicures take 45-60 minutes.",
      "When you leave, your nails are completely dry and ready to go — no smudging risk! Gel cures under the lamp, so there's zero drying time. Show them off immediately. Book your first gel manicure at vagaro.com/thenailladie or call (541) 992-1887."]),

    ("Nail Stamping Tutorial: How It Works", "nail-stamping-tutorial-how-it-works",
     "How does nail stamping work? Step-by-step tutorial from The Nail Ladie in Depoe Bay. Learn about this popular nail art technique.",
     "nail stamping tutorial", "educational",
     ["Nail stamping is one of the most fascinating nail art techniques, and it's a specialty at The Nail Ladie in Depoe Bay. But how does it actually work? Here's a step-by-step look at the stamping process.",
      "Step 1: Choose a stamping plate. These are thin metal plates with designs etched into them — everything from florals and geometric patterns to text, landscapes, and holiday themes. The Nail Ladie has an extensive collection of stamping plates with hundreds of designs to choose from.",
      "Step 2: Apply stamping polish. A special, highly pigmented polish is brushed over the design on the plate. Regular nail polish is too thin — stamping polish is formulated to be thick and opaque for crisp transfers. The excess polish is scraped away, leaving polish only in the etched grooves.",
      "Step 3: Pick up the design. A soft silicone stamper is pressed onto the plate, picking up the polish pattern from the grooves. The design transfers to the stamper in perfect detail — every line, every curve, every tiny detail.",
      "Step 4: Apply to nail. The stamper is rolled onto the nail surface, depositing the design in one clean motion. The result is a crisp, detailed pattern that would be nearly impossible to paint freehand. Once dry, it's sealed with a top coat for durability. See stamping in action on our Instagram @the_nail_ladie, and book a stamped design at vagaro.com/thenailladie."]),

    ("Cuticle Care: Why It Matters for Healthy Nails", "cuticle-care-guide-healthy-nails",
     "The importance of cuticle care for healthy, beautiful nails. Expert advice from The Nail Ladie in Depoe Bay, Oregon.",
     "cuticle care", "educational",
     ["Your cuticles might seem like a small detail, but they play a huge role in nail health and the longevity of your manicure. At The Nail Ladie in Depoe Bay, proper cuticle care is a foundation of every service we offer. Here's why it matters.",
      "Your cuticle is the thin layer of skin at the base of your nail that acts as a seal between your nail plate and the surrounding skin. It protects against bacteria, fungi, and infections. Healthy cuticles mean healthy nails — it's that simple.",
      "What not to do: never cut your cuticles with clippers at home. Cutting creates tiny wounds that can become infected and causes the cuticle to grow back thicker and faster. Instead, gently push cuticles back after a shower when they're soft, using a wooden orange stick or rubber-tipped pusher.",
      "Daily cuticle oil is the single best thing you can do for your nails at home. Apply a drop of cuticle oil to each nail before bed and massage it in. This keeps the cuticle flexible, prevents hangnails, and nourishes the nail matrix (where new nail growth starts). Jojoba, vitamin E, and sweet almond oil are all excellent choices.",
      "At The Nail Ladie, every manicure includes professional cuticle care — gentle pushing, exfoliation, and hydration. We also offer a dedicated Cuticle Treatment add-on. Healthy cuticles = beautiful nails. Book at vagaro.com/thenailladie."]),

    ("What Is a Lash Lift? Everything You Need to Know", "what-is-a-lash-lift-guide",
     "What is a lash lift? Complete guide from The Nail Ladie in Depoe Bay. How it works, how long it lasts, and who it's best for.",
     "lash lift guide", "educational",
     ["A lash lift is one of the easiest, most low-maintenance beauty treatments available — and it's perfect for Oregon Coast living. Here's everything you need to know about lash lifts from The Nail Ladie in Depoe Bay.",
      "A lash lift is essentially a semi-permanent curl for your natural eyelashes. Using a silicone shield and a gentle perming solution, your lashes are lifted from the root and set into a beautifully curled shape. No extensions, no glue, no daily maintenance.",
      "The process takes about 45-60 minutes. You'll lie comfortably with your eyes closed while Heather applies the lifting solution. It's completely painless — most clients find it so relaxing they doze off! The results are visible immediately: lifted, curled lashes that make your eyes look wider and more awake.",
      "Results last 6-8 weeks, depending on your natural lash growth cycle. As your lashes naturally shed and regrow, the lift gradually returns to your natural curl pattern. Many clients rebook every 6-8 weeks to maintain their lifted look year-round.",
      "We pair every lash lift with a professional tint that darkens your lashes for an even more dramatic effect — no mascara needed. The combination is perfect for active lifestyles: swimming, rain, tears — nothing affects a lash lift. Book yours at vagaro.com/thenailladie or call (541) 992-1887."]),

    ("Nail Health: Signs of Healthy vs Unhealthy Nails", "nail-health-signs-healthy-unhealthy-nails",
     "How to tell if your nails are healthy. Signs of nail problems and what they mean. Expert advice from The Nail Ladie in Depoe Bay.",
     "nail health signs", "educational",
     ["Your nails can tell you a lot about your overall health. At The Nail Ladie in Depoe Bay, Heather always assesses nail health before starting any service. Here's what to look for and what common nail changes might mean.",
      "Signs of healthy nails: smooth, even surface with no ridges or pits. Consistent pink color across the nail bed. Cuticles that are intact and not inflamed. Nails that are firm but slightly flexible. White tips that are even and consistent.",
      "Common concerns: vertical ridges running from cuticle to tip are usually a normal sign of aging — not a cause for concern. Horizontal ridges (Beau's lines) can indicate a past illness, injury, or nutrient deficiency. White spots are typically caused by minor trauma to the nail matrix and grow out on their own.",
      "Red flags to watch: persistent yellowing may indicate a fungal infection. Nails that separate from the nail bed need professional attention. Dark streaks under the nail should be evaluated by a dermatologist. Nails that are extremely brittle, thin, or spoon-shaped may indicate nutritional deficiencies.",
      "At The Nail Ladie, we prioritize nail health alongside beauty. If Heather notices any concerns during your appointment, she'll let you know. Healthy nails are beautiful nails. Book at vagaro.com/thenailladie or call (541) 992-1887."]),

    # 51-65: Comparison & Lifestyle
    ("Regular Polish vs Gel Polish: Why Switch to Gel?", "regular-polish-vs-gel-polish-comparison",
     "Regular nail polish vs gel polish — why more Oregon Coast women are switching to gel. Comparison from The Nail Ladie in Depoe Bay.",
     "regular vs gel polish", "comparison",
     ["Still using regular nail polish? Here's why thousands of Oregon Coast women have made the switch to gel — and why you might want to, too. From longevity to shine, gel polish outperforms traditional polish in nearly every way.",
      "Longevity: Regular polish chips within 3-7 days. Gel polish lasts 2-3 weeks without a single chip. If you're tired of repainting your nails every weekend, gel is a game-changer. One appointment at The Nail Ladie and you're set for weeks.",
      "Finish: Gel polish maintains its high-gloss shine from day one to day twenty-one. Regular polish starts dulling and losing its luster within days. That fresh-from-the-salon look? With gel, it lasts.",
      "Drying time: Regular polish takes 20-30 minutes to fully dry and can smudge even after that. Gel polish cures under LED light in 30-60 seconds. When you leave The Nail Ladie, your nails are completely set — grab your keys, text your friends, no risk of smudging.",
      "Cost comparison: A gel-polish manicure at The Nail Ladie is $35, lasting 2-3 weeks. A regular polish manicure might be cheaper per visit, but if you're repainting weekly, the cost adds up — and so does the time. Gel is more cost-effective over time. Try it at vagaro.com/thenailladie."]),

    ("Wedding Nails on the Oregon Coast", "wedding-nails-oregon-coast",
     "Wedding nail designs at The Nail Ladie in Depoe Bay. Bridal manicures, bridesmaid nails, and mother-of-the-bride looks for Oregon Coast weddings.",
     "wedding nails", "lifestyle",
     ["Getting married on the Oregon Coast? Your nails will be in every photo — the ring shot, the bouquet toss, the first dance hand-hold. At The Nail Ladie in Depoe Bay, Heather creates stunning bridal nail designs that photograph beautifully and last through your entire wedding weekend.",
      "Popular bridal nail styles include classic French tips (timeless and elegant), soft pink or nude gel (photography-perfect), delicate lace stamping (romantic and unique), pearl and crystal accents (glamorous), and white ombre (modern and fresh). Each look can be customized to match your wedding palette.",
      "For the bride, we recommend booking a trial appointment 2-4 weeks before the wedding. This gives you and Heather time to test designs, finalize colors, and make adjustments. On the trial, bring a photo of your dress, your bouquet inspiration, and any nail ideas you love.",
      "Bridesmaids and mothers of the bride are welcome too! We can coordinate complementary nail looks for the whole wedding party. Book back-to-back appointments or spread them across the week before the wedding. Group bookings are easy — just call to arrange.",
      "Oregon Coast wedding season books up fast! Reserve your bridal nail appointments early at vagaro.com/thenailladie or call (541) 992-1887."]),

    ("Self-Care Day in Depoe Bay: Nails, Lashes & Coastal Vibes", "self-care-day-depoe-bay-nails-lashes",
     "Plan the perfect self-care day in Depoe Bay, Oregon. Nails and lashes at The Nail Ladie, plus whale watching, dining, and beach time.",
     "self-care day Depoe Bay", "lifestyle",
     ["Sometimes you need a day that's all about you. Depoe Bay, Oregon, is the perfect setting for a self-care day — and it starts at The Nail Ladie. Here's how to plan the ultimate pampering day on the Oregon Coast.",
      "Start your morning at The Nail Ladie with a gel manicure and pedicure combo. Let Heather work her magic while you relax in our private, one-on-one salon. Add a lash lift and tint for the ultimate refresh — by lunch, you'll look and feel amazing without a single minute of daily maintenance ahead.",
      "After your appointment, step outside and you're in the heart of Depoe Bay. Walk to the seawall and watch for gray whales — Depoe Bay is the Whale Watching Capital of the Oregon Coast, and resident whales are often visible from shore. The Spouting Horn natural geyser is steps away.",
      "For lunch, grab chowder or fish and chips at one of Depoe Bay's waterfront restaurants. The views are stunning, and you can admire your fresh nails while sipping a glass of Oregon Pinot. After lunch, browse the charming shops and galleries along the bay.",
      "End your day with a walk along the coastline or a drive to nearby Boiler Bay for a sunset viewpoint. Self-care at its finest — and it all started at The Nail Ladie. Book your pampering day at vagaro.com/thenailladie."]),

    ("Prom Nails: Nail Art Ideas for Prom Season", "prom-nails-ideas-oregon-coast",
     "Prom nail art ideas from The Nail Ladie in Depoe Bay. Match your dress, stand out in photos, and feel amazing on prom night.",
     "prom nails", "lifestyle",
     ["Prom night is your moment to shine, and your nails should be part of the look. At The Nail Ladie in Depoe Bay, Heather creates custom prom nail designs that match your dress, your style, and your personality.",
      "Popular prom nail ideas include color-matching your dress with a gel manicure ($35), adding glitter or chrome accents for extra sparkle, trying a longer length with Gel-X extensions ($110) for that dramatic prom look, or going all-out with custom nail art featuring rhinestones, foils, and hand-painted designs.",
      "Pro tips for prom nails: bring a photo or swatch of your dress fabric to your appointment so Heather can color-match perfectly. Book your appointment 1-2 days before prom — not the day of, in case you need any adjustments. And consider getting a pedicure too, especially if you're wearing open-toe heels!",
      "Student-friendly pricing: a gel manicure with simple nail art starts at $50 (base gel mani $35 + Tier 1 art $15). Even our most elaborate custom designs are just $95 (base + Tier 4 art). Every budget can get gorgeous prom nails at The Nail Ladie.",
      "Book your prom appointment early — spring is busy season! Visit vagaro.com/thenailladie or call (541) 992-1887."]),

    ("Mother's Day Gift: Treat Mom to The Nail Ladie", "mothers-day-gift-nail-salon-depoe-bay",
     "Give Mom the gift of beautiful nails this Mother's Day. Gift certificates and pampering appointments at The Nail Ladie in Depoe Bay.",
     "Mother's Day gift nails", "lifestyle",
     ["This Mother's Day, skip the flowers and give Mom something she'll truly enjoy: a pampering session at The Nail Ladie in Depoe Bay. Because every mom deserves to feel beautiful, relaxed, and appreciated.",
      "The most popular Mother's Day gift is a gel manicure appointment ($35) — a treat Mom might not buy for herself but absolutely deserves. For an upgraded experience, book her a Classic Pedicure with Gel Polish ($85) or a combo manicure and pedicure for the ultimate pampering session.",
      "Want to make it extra special? Book a mother-daughter appointment! Heather can schedule back-to-back slots so you can enjoy the experience together. Spend quality time in our peaceful private salon, then head to a Depoe Bay restaurant for brunch.",
      "Gift certificates are available for any service or dollar amount. Call The Nail Ladie at (541) 992-1887 to purchase a gift certificate. It's the perfect last-minute gift for the mom who has everything.",
      "This Mother's Day, give the gift of self-care. Book at vagaro.com/thenailladie."]),

    ("Date Night Nails: Look Your Best for a Night Out", "date-night-nails-depoe-bay",
     "Date night nails at The Nail Ladie in Depoe Bay. Bold, confident, head-turning manicures for your night out on the Oregon Coast.",
     "date night nails", "lifestyle",
     ["Date night deserves special nails. Whether it's a first date, an anniversary dinner, or a spontaneous night out on the Oregon Coast, The Nail Ladie in Depoe Bay will have you looking and feeling your most confident.",
      "Date night nail favorites include deep red gel (classic and sexy), dark cherry or wine tones (sophisticated), black with gold chrome accent (edgy and bold), nude with rhinestone details (understated glamour), and cat eye in deep emerald or sapphire (mysterious and captivating).",
      "For something extra eye-catching, try mirror chrome nails. The reflective metallic finish is guaranteed to catch the candlelight — and your date's attention. Available in rose gold, silver, champagne, and more.",
      "Short on time? A gel-polish manicure takes just 45-50 minutes and you'll leave with completely dry, smudge-proof nails. Call The Nail Ladie at (541) 992-1887 to check same-day availability.",
      "Look your best tonight. Book at vagaro.com/thenailladie."]),

    # 56-70: Trends & Techniques
    ("Nail Art Trends 2026: What's Hot This Year", "nail-art-trends-2026",
     "The biggest nail art trends of 2026 from The Nail Ladie in Depoe Bay. Chrome, glazed donuts, aura nails, 3D art, and more.",
     "nail art trends 2026", "trends",
     ["Nail art in 2026 is bolder, more creative, and more expressive than ever. At The Nail Ladie in Depoe Bay, Heather stays on the cutting edge of nail trends — here are the biggest looks she's seeing (and creating) this year.",
      "Glazed Donut Nails: This Hailey Bieber-inspired trend continues to dominate. A sheer nude or pink base with a chrome powder overlay creates a luminous, pearlescent finish that looks like a glazed donut. It's elegant, modern, and flattering on everyone.",
      "Aura Nails: Soft, airbrushed color gradients centered on the nail create a dreamy, ethereal effect. Think pastel purple fading into pink, or soft blue into white. Aura nails are perfect for clients who want something artistic but wearable.",
      "3D Nail Art: Textured elements like raised flowers, bows, pearls, and geometric shapes are trending hard. These dimensional accents add a sculptural quality to your nails that flat art can't achieve.",
      "Chrome Everything: Chrome isn't going anywhere. New chrome finishes include velvet chrome (matte metallic), magnetic chrome (combines chrome with cat eye), and gradient chrome (different metallic at tip and base). Book any of these trends at vagaro.com/thenailladie."]),

    ("Ombre Nails: Gradient Nail Art Explained", "ombre-nails-gradient-nail-art",
     "Ombre nails at The Nail Ladie in Depoe Bay. How gradient nail art is created and the most popular ombre styles on the Oregon Coast.",
     "ombre nails", "trends",
     ["Ombre nails — that beautiful gradient fade from one color to another — are one of the most requested nail art styles at The Nail Ladie in Depoe Bay. The effect is eye-catching, versatile, and looks stunning at any nail length.",
      "How ombre nails are created: Heather applies two or more gel colors and blends them together using a special sponge or brush technique. The colors seamlessly transition from one to another, creating a smooth gradient. The blending is done before curing, so the colors meld perfectly.",
      "Popular ombre combinations include: nude to white (classic baby boomer/French ombre), pink to white (bridal favorite), black to glitter (dramatic evening look), two-tone pastels (spring/summer vibes), coral to gold (sunset inspired), and teal to seafoam (Oregon Coast inspired!).",
      "Ombre works on any nail length and shape. On shorter nails, a subtle two-tone ombre looks elegant and elongating. On longer extensions, multi-color ombre gradients make a bold statement. Add chrome powder over an ombre base for an extra dimension of color shifting.",
      "Get your perfect ombre at The Nail Ladie. Book at vagaro.com/thenailladie or call (541) 992-1887."]),

    ("French Tip Nails: Classic to Modern Variations", "french-tip-nails-modern-variations",
     "French tip nails at The Nail Ladie in Depoe Bay. Classic white tips and modern variations — colored, chrome, ombre, and artistic French designs.",
     "French tip nails", "trends",
     ["The French manicure is the most timeless nail design in the world — and at The Nail Ladie in Depoe Bay, we've taken it far beyond the classic white tip. Here's a look at French tip styles, from traditional to totally modern.",
      "Classic French: The original — natural pink base with clean white tips. It's elegant, professional, and never goes out of style. Perfect for job interviews, weddings, and everyday wear. French tip upgrade is available on any manicure service for $15.",
      "Colored French: Replace the white tip with any color. Popular choices include black (edgy modern), red (dramatic), neon (fun summer look), metallic gold or silver (glamorous), and deep green or burgundy (seasonal). Same technique, completely different vibe.",
      "Chrome French: A metallic chrome tip over a nude or sheer base. This modern take on the French manicure catches the light beautifully and looks incredibly luxurious. Rose gold chrome tips are a particular favorite.",
      "Ombre French (Baby Boomer): Instead of a sharp line between the base and tip, the white is blended into the pink for a soft, gradient transition. This creates a more natural, subtle French look that's incredibly popular right now. Book your French nails at vagaro.com/thenailladie."]),

    ("Glitter Nails: Sparkle and Shine at The Nail Ladie", "glitter-nails-sparkle-shine-depoe-bay",
     "Glitter nails at The Nail Ladie in Depoe Bay. Full glitter sets, glitter ombre, and glitter accent nails on the Oregon Coast.",
     "glitter nails", "trends",
     ["Glitter nails never go out of style. At The Nail Ladie in Depoe Bay, we offer multiple ways to add sparkle to your manicure — from subtle shimmer to full-on glitter bomb. Here are the most popular glitter nail options.",
      "Full glitter set: Every nail covered in glitter for maximum sparkle. Glitter gel or loose glitter is encapsulated in clear gel for a smooth finish that won't snag. Available in fine or chunky glitter, in every color imaginable. Perfect for holidays, parties, and anyone who loves to shine.",
      "Glitter ombre: Glitter concentrated at the tips or base, fading into a solid color. This creates a more wearable, everyday sparkle that's still eye-catching. Gold glitter fading from nude tips is a client favorite.",
      "Glitter accent nail: One or two nails get the full glitter treatment while the rest are a complementary solid color. This is the most popular glitter option — all the sparkle, perfectly balanced.",
      "At The Nail Ladie, glitter looks are created using a variety of products: glitter gel, loose glitter, chunky glitter mix, holographic glitter, and color-shifting glitter. Heather will help you choose the right sparkle level for your style. Book at vagaro.com/thenailladie."]),

    ("Matte Nails: The Understated Trend", "matte-nails-trend-depoe-bay",
     "Matte finish nails at The Nail Ladie in Depoe Bay. Velvety, sophisticated matte nail looks on the Oregon Coast.",
     "matte nails", "trends",
     ["Matte nails offer a completely different vibe from traditional glossy polish. The velvety, flat finish looks sophisticated, modern, and unexpectedly luxurious. At The Nail Ladie in Depoe Bay, matte finishes are available on any gel manicure service.",
      "How it works: a matte top coat is applied over your gel color and cured. Instead of the usual high-gloss shine, the result is a smooth, satiny finish that absorbs light rather than reflecting it. Any color can be made matte — but some look especially stunning.",
      "Colors that shine in matte: black matte is bold and powerful. Deep red matte is sultry and dramatic. Nude or blush matte is minimal and chic. Dark green or navy matte is moody and sophisticated. Even chrome nails can be finished with a matte top coat for a velvet metallic effect — pure luxury.",
      "Matte mix: try combining matte and glossy on the same hand. Glossy accent nails with matte base color (or vice versa) creates a sophisticated, textured look. Or go with matte nails with glossy stamped designs for dimension.",
      "Try matte at your next appointment at The Nail Ladie. Book at vagaro.com/thenailladie or call (541) 992-1887."]),

    ("Nude Nails: Why Neutrals Never Go Out of Style", "nude-nails-neutrals-depoe-bay",
     "Nude and neutral nail colors at The Nail Ladie in Depoe Bay. The timeless, versatile choice for every occasion.",
     "nude nails", "trends",
     ["Nude nails are the little black dress of the manicure world — they go with everything, suit every occasion, and never look dated. At The Nail Ladie in Depoe Bay, neutral shades are consistently among our most requested colors. Here's why.",
      "The beauty of nude nails is their versatility. The same manicure that's appropriate for a job interview looks equally at home at a beachside dinner, a wedding, or a casual brunch. You never have to worry about your nails clashing with your outfit or being too much for a particular occasion.",
      "Finding your perfect nude: nude nail shades range from pale pink to warm beige to deep caramel, and the right one depends on your skin tone. Heather will help you find the nude that complements your complexion — whether that's a cool-toned milky pink, a warm peachy nude, or a rich chocolate for deeper skin tones.",
      "Elevating nude nails: nude doesn't have to mean basic. Add a chrome powder for a glazed donut effect. Try a nude-to-white French ombre. Mix matte and glossy finishes. Add a single rhinestone or gold flake accent. These subtle details take nude nails from simple to stunning.",
      "Timeless, elegant, always appropriate. Book your nude manicure at vagaro.com/thenailladie."]),

    # 61-70: More trends/techniques
    ("Nail Art for Short Nails: You Don't Need Length", "nail-art-short-nails-ideas",
     "Nail art isn't just for long nails. The Nail Ladie in Depoe Bay creates stunning designs on short, natural nails. Ideas and inspiration.",
     "nail art short nails", "trends",
     ["Think you need long nails for great nail art? Think again. At The Nail Ladie in Depoe Bay, some of our most stunning work is done on short, natural nails. Here's why short nails are actually a perfect canvas for nail art.",
      "Short nails have an advantage: they're low-maintenance, practical, and sturdy. You don't have to worry about breakage, and they work perfectly for active Oregon Coast lifestyles. And with the right design, short nails look absolutely gorgeous.",
      "Best nail art styles for short nails: minimalist line art (a single delicate line or geometric shape), micro French tips (thin white or colored tips that elongate the nail), single accent features (one rhinestone, one dot, one tiny stamped design), color blocking (two complementary colors divided by a clean line), and negative space designs (leaving part of the nail natural).",
      "Colors that flatter short nails: darker colors actually make short nails look longer. Try deep berry, navy, emerald, or classic red. Nude and blush shades create a seamless, elongating effect. Avoid very pale or very chunky glitter on short nails, as they can make nails look wider.",
      "Short nails, big style. Book at vagaro.com/thenailladie or call (541) 992-1887."]),

    ("Marble Nail Art: Stone-Inspired Designs", "marble-nail-art-designs-depoe-bay",
     "Marble nail art at The Nail Ladie in Depoe Bay. Elegant stone-inspired nail designs that look like natural marble.",
     "marble nail art", "trends",
     ["Marble nail art brings the beauty of natural stone to your fingertips — literally. At The Nail Ladie in Depoe Bay, Heather creates stunning marble effects using a combination of gel polish, fine detail brushes, and stamping techniques.",
      "Classic white marble: a white or off-white base with thin grey and gold veining mimics Carrara marble. This look is elegant, sophisticated, and incredibly popular for weddings, special occasions, and everyday elegance.",
      "Colored marble: the marble technique works with any color palette. Dark green marble looks like malachite. Deep blue resembles lapis lazuli. Pink marble is romantic and feminine. Black marble with gold veining is dramatic and luxurious.",
      "Marble can be applied to all ten nails for a cohesive look, or used as accent nails paired with a complementary solid color. Two marble accent nails with eight solid nails is a popular combination that adds visual interest without overwhelming.",
      "Book marble nail art at The Nail Ladie — our tiered pricing means you can get simple marble accents (Tier 1, $15) or elaborate all-over marble designs (Tier 2-3, $25-$50). Visit vagaro.com/thenailladie."]),

    ("Floral Nail Art: Hand-Painted and Stamped Flowers", "floral-nail-art-flowers-depoe-bay",
     "Floral nail art at The Nail Ladie in Depoe Bay. Hand-painted roses, stamped wildflowers, and botanical nail designs.",
     "floral nail art", "trends",
     ["Floral nail art is a perennial favorite at The Nail Ladie in Depoe Bay — pun absolutely intended. From delicate stamped wildflowers to elaborate hand-painted roses, flower designs add a feminine, artistic touch to any manicure.",
      "Stamped florals: our extensive stamping plate collection includes dozens of floral designs — cherry blossoms, sunflowers, roses, daisies, tropical flowers, and abstract botanical patterns. Stamped flowers are crisp, consistent, and can be applied quickly, making them a great option for every-nail designs.",
      "Hand-painted florals: for truly custom work, Heather hand-paints flowers using fine detail brushes. Hand-painted designs have an organic, watercolor quality that stamping can't replicate. Each flower is slightly different — just like in nature.",
      "Popular floral combinations: lavender fields on nude nails, pink roses on white with gold foil, sunflowers on clear negative-space nails, cherry blossoms on soft pink for spring, and dark moody florals (deep red roses on black) for fall and winter.",
      "Floral nail art starts at Tier 1 ($15) for simple stamped accents and goes up to Tier 4 ($60) for full custom hand-painted botanical designs. Book at vagaro.com/thenailladie."]),

    ("Abstract Nail Art: Artistic and Unique Designs", "abstract-nail-art-unique-designs",
     "Abstract nail art at The Nail Ladie in Depoe Bay. Unique, artistic designs including swirls, color blocking, and modern art nails.",
     "abstract nail art", "trends",
     ["Abstract nail art is for clients who see their nails as a canvas. At The Nail Ladie in Depoe Bay, Heather creates unique abstract designs that are wearable art — no two sets ever the same.",
      "Abstract nail art includes: free-form swirls and lines in contrasting colors, color blocking with bold geometric shapes, watercolor washes that blend and bleed beautifully, splatter and drip effects, wavy lines and organic shapes, and mixed-media looks combining multiple techniques.",
      "The beauty of abstract nail art is that there are no rules. Unlike a French tip or a stamped pattern, abstract designs are truly one-of-a-kind. Heather uses her artistic eye to create compositions that are balanced, intentional, and always stylish.",
      "Abstract designs work at every price point. Simple abstract accents (a single swirl or color block) fall into Tier 1 ($15). More complex multi-color abstracts are Tier 2 ($25) or Tier 3 ($50). Full custom abstract art — where every nail is a unique composition — is Tier 4 ($60).",
      "Express yourself through your nails. Book abstract art at vagaro.com/thenailladie or call (541) 992-1887."]),

    ("Minimalist Nail Art: Less Is More", "minimalist-nail-art-depoe-bay",
     "Minimalist nail art at The Nail Ladie in Depoe Bay. Clean lines, subtle accents, and understated elegance.",
     "minimalist nail art", "trends",
     ["Minimalist nail art proves that less really is more. At The Nail Ladie in Depoe Bay, some of our most impactful designs use the simplest elements — a single line, a tiny dot, a subtle accent that catches the eye without shouting.",
      "Popular minimalist nail designs include: a thin metallic line at the cuticle or across the middle of the nail, tiny dots in a constellation pattern, single small geometric shapes, half-moon designs at the base or tip, and micro text or symbols.",
      "Minimalist nail art pairs beautifully with nude, blush, or sheer base colors. The subtle detail against a clean base creates an effortlessly chic look that's appropriate for any setting — professional, casual, or dressy.",
      "The minimalist approach also works with negative space designs, where part of the natural nail is left bare as part of the design. Clear gaps, geometric cutouts, and half-painted nails all fall into this artistic category.",
      "Minimalist doesn't mean boring — it means intentional. Book minimalist nail art at The Nail Ladie. Simple designs start at Tier 1 ($15). Visit vagaro.com/thenailladie."]),

    # 71-85: Local tourism tie-ins
    ("Things to Do in Depoe Bay After Your Nail Appointment", "things-to-do-depoe-bay-after-nails",
     "What to do in Depoe Bay after your appointment at The Nail Ladie. Whale watching, dining, shopping, and coastal activities.",
     "things to do Depoe Bay", "tourism",
     ["Your nails look amazing — now explore the charming town they were created in. Depoe Bay, Oregon, is one of the most delightful small towns on the entire Pacific Coast. Here's what to do after your appointment at The Nail Ladie.",
      "Whale Watching: Depoe Bay is officially the Whale Watching Capital of the Oregon Coast. Resident gray whales are visible from the seawall year-round. For a closer look, book a whale watching charter from the harbor — several operators depart daily. It's an unforgettable experience.",
      "The Spouting Horn: Just steps from our salon, this natural phenomenon sends ocean swells blasting through rocky channels, creating dramatic spray that can reach 30 feet high. Best during high tide and stormy weather — but impressive any time.",
      "Dining: Depoe Bay has excellent seafood restaurants. Try fresh clam chowder, fish and chips, or Dungeness crab at one of the waterfront spots. Many restaurants offer ocean views that pair perfectly with your meal.",
      "The World's Smallest Harbor: Depoe Bay's harbor is recognized as the world's smallest navigable harbor. It's incredibly photogenic and a perfect spot to admire your fresh nails with an ocean backdrop. For more adventures, Boiler Bay State Scenic Viewpoint is just minutes north. Book your Depoe Bay experience at vagaro.com/thenailladie."]),

    ("Whale Watching and Spa Day in Depoe Bay", "whale-watching-spa-day-depoe-bay",
     "Combine whale watching with a spa day at The Nail Ladie in Depoe Bay. The perfect Oregon Coast day trip itinerary.",
     "whale watching spa day", "tourism",
     ["Planning a perfect day on the Oregon Coast? Combine whale watching in Depoe Bay with a pampering spa session at The Nail Ladie. Here's your ultimate Depoe Bay day trip itinerary.",
      "Morning (9-10 AM): Start with a whale watching charter from Depoe Bay harbor. Several operators offer 1-2 hour trips that head out past the harbor channel to where gray whales feed. Peak whale watching season is December-January (migration) and March-May (returning north with calves), but resident whales are visible year-round.",
      "Late Morning (11 AM): Head to The Nail Ladie for your appointment. A gel manicure takes about 45-50 minutes, or combine it with a pedicure for a longer pampering session. After the ocean air, your hands and feet will love the attention.",
      "Lunch (12:30 PM): Walk to one of Depoe Bay's waterfront restaurants for fresh seafood. Clam chowder is a must. Sit outside if weather permits and watch for whale spouts from the seawall while you eat.",
      "Afternoon: Browse the shops along Highway 101, visit the Spouting Horn, or drive 10 minutes north to Boiler Bay for a cliffside walk with dramatic ocean views. Your fresh nails will look perfect in every photo. Book your spa portion at vagaro.com/thenailladie."]),

    ("Oregon Coast Road Trip Beauty Stop: Depoe Bay", "oregon-coast-road-trip-beauty-stop-depoe-bay",
     "On an Oregon Coast road trip? Stop at The Nail Ladie in Depoe Bay for a quick beauty refresh. Right on Highway 101.",
     "Oregon Coast road trip", "tourism",
     ["Driving the Oregon Coast? Depoe Bay is one of the most scenic stops on Highway 101 — and it's home to The Nail Ladie, the perfect place to treat yourself to a beauty refresh mid-road-trip.",
      "The Nail Ladie is located right on Highway 101 at 531 US-101 Suites K1-2. Easy pull-in parking, no detour required. Whether you're driving from Portland to the southern coast, or doing a Lincoln City-to-Newport loop, Depoe Bay is a natural stopping point.",
      "Quick road trip services: a gel-polish manicure ($35) takes just 45-50 minutes and gives you chip-free nails for the rest of your trip. A polish change ($15) is even quicker. Or treat your road-weary feet to a Petite Pedicure ($35) before hitting the highway again.",
      "While you're in Depoe Bay, take 30 minutes to explore. Walk to the seawall to look for whales, see the Spouting Horn, grab a quick bowl of chowder, and snap some photos at the world's smallest harbor. It's one of the best short stops on the entire Oregon Coast.",
      "Planning your road trip? Book your Depoe Bay beauty stop in advance at vagaro.com/thenailladie or call (541) 992-1887."]),

    ("Depoe Bay Bridge: Iconic Oregon Coast Landmark", "depoe-bay-bridge-iconic-landmark",
     "The historic Depoe Bay Bridge is steps from The Nail Ladie salon. Learn about this iconic Oregon Coast landmark.",
     "Depoe Bay Bridge", "tourism",
     ["The Depoe Bay Bridge is one of the most photographed landmarks on the Oregon Coast — and it's just steps from The Nail Ladie salon. This iconic arched bridge spans the channel of the world's smallest navigable harbor, connecting the two sides of Depoe Bay along Highway 101.",
      "Built in 1927 by legendary Oregon bridge designer Conde McCullough, the Depoe Bay Bridge is a masterpiece of Art Deco-influenced concrete engineering. Its graceful arch frames the narrow harbor entrance below, where fishing boats and whale watching charters navigate the dramatic channel.",
      "The bridge offers some of the best viewpoints in Depoe Bay. Walk across and look down at the harbor, the crashing waves, and the channel walls. On the south side, you can watch boats enter and exit the harbor through the narrow passage — a thrilling sight during rough seas.",
      "After your nail appointment at The Nail Ladie, the bridge is a perfect first stop for a Depoe Bay walkabout. Your fresh nails will look stunning in photos with the bridge and harbor as backdrop. Continue along the seawall toward the Spouting Horn for more coastal views.",
      "Visit Depoe Bay and treat yourself at The Nail Ladie. Book at vagaro.com/thenailladie."]),

    ("Boiler Bay to Depoe Bay: Coastal Walk and Nails", "boiler-bay-coastal-walk-nails-depoe-bay",
     "Combine a Boiler Bay scenic walk with a nail appointment at The Nail Ladie in Depoe Bay. Nature and beauty on the Oregon Coast.",
     "Boiler Bay Depoe Bay", "tourism",
     ["Boiler Bay State Scenic Viewpoint, just minutes north of Depoe Bay, offers some of the most dramatic coastal scenery on the Oregon Coast. Pair a Boiler Bay visit with a nail appointment at The Nail Ladie for the perfect day.",
      "Boiler Bay earned its name from the steam boiler of a shipwrecked freighter that was visible on the rocks for decades. Today, the viewpoint features rugged cliffs, crashing waves, tide pools, and incredible sunset views. Short walking paths wind along the clifftops — wear sturdy shoes.",
      "Start your morning with a walk at Boiler Bay, then head 5 minutes south to Depoe Bay for your nail appointment at The Nail Ladie. After your nails are done, explore Depoe Bay's harbor, shops, and restaurants.",
      "Boiler Bay is also one of the best spots for storm watching on the Oregon Coast. During winter storms, massive waves crash against the basalt cliffs and send spray dozens of feet into the air. After storm watching, warm up at The Nail Ladie and treat yourself to a pampering manicure.",
      "Plan your coastal day at vagaro.com/thenailladie or call (541) 992-1887."]),

    ("Nye Beach Newport and Nails in Depoe Bay", "nye-beach-newport-nails-depoe-bay",
     "Combine a trip to Nye Beach in Newport with a nail appointment at The Nail Ladie in Depoe Bay. Art, dining, and beauty on the Oregon Coast.",
     "Nye Beach Newport", "tourism",
     ["Nye Beach in Newport is one of the most charming neighborhoods on the Oregon Coast — galleries, cafes, and the stunning beach itself. Combine a Nye Beach day with a nail appointment at The Nail Ladie in Depoe Bay, just 15 minutes north.",
      "Start your day at The Nail Ladie in Depoe Bay with a gel manicure. With your nails freshly done and photo-ready, head south to Newport's Nye Beach. Browse the art galleries, grab a coffee at a beachfront cafe, and walk the sandy beach.",
      "Nye Beach is also home to the Performing Arts Center and the Newport Visual Arts Center. After your Depoe Bay nail appointment, you can enjoy an afternoon of culture, art, and ocean views.",
      "For the full day, hit both the Nye Beach area and the Bayfront in Newport. The Bayfront has sea lion viewing, the Oregon Coast Aquarium, Hatfield Marine Science Center, and excellent seafood restaurants. With fresh nails from The Nail Ladie, every experience is a little more special.",
      "Book your Depoe Bay nail appointment at vagaro.com/thenailladie, then plan your Newport adventure."]),

    # 76-85: More tourism + misc
    ("Depoe Bay Restaurants: Where to Eat After Your Nails", "depoe-bay-restaurants-after-nails",
     "Best restaurants in Depoe Bay near The Nail Ladie. Where to eat after your nail appointment on the Oregon Coast.",
     "Depoe Bay restaurants", "tourism",
     ["Fresh nails deserve a celebratory meal. Luckily, Depoe Bay has some of the best dining on the Oregon Coast — and most restaurants are walking distance from The Nail Ladie. Here's where to eat after your appointment.",
      "Depoe Bay is famous for its seafood. Fresh clam chowder, Dungeness crab, fish and chips, and pan-seared salmon are all Oregon Coast specialties. Many restaurants source directly from local fishermen, so the seafood is as fresh as it gets.",
      "Several restaurants along Highway 101 and the harbor offer ocean views. Dining with a view of the harbor, the bridge, and the Pacific Ocean makes any meal more memorable. Some spots even have outdoor seating during warmer months — perfect for showing off your new nails.",
      "For a casual bite, grab chowder in a bread bowl from a waterfront stand. For a nicer sit-down experience, several restaurants offer full menus with wine lists featuring Oregon Pinot Noir and Pinot Gris. Either way, your post-nail meal in Depoe Bay will be delicious.",
      "Make it a full experience: nails at The Nail Ladie, then lunch in Depoe Bay. Book at vagaro.com/thenailladie."]),

    ("Oregon Coast Tide Pools: Adventure After Your Appointment", "oregon-coast-tide-pools-depoe-bay",
     "Explore Oregon Coast tide pools near Depoe Bay after your nail appointment at The Nail Ladie. Nature and beauty combined.",
     "tide pools Oregon Coast", "tourism",
     ["The Oregon Coast near Depoe Bay is home to some of the most incredible tide pools in the Pacific Northwest. After your nail appointment at The Nail Ladie, head to the coast for a tide pool adventure — just be careful with those fresh nails!",
      "The best tide pooling near Depoe Bay is at Otter Rock (15 minutes south), where the Devil's Punchbowl area offers accessible rocky shoreline pools teeming with sea stars, anemones, urchins, crabs, and small fish. Low tide is the best time — check tide charts before heading out.",
      "Depoe Bay itself has rocky shoreline areas where you can spot marine life at low tide. The areas south of the bridge, near the Spouting Horn, often have tide pools in the basalt formations.",
      "Pro tip for nail lovers: gel nails and structured gel are perfect for outdoor Oregon Coast activities. They resist chips and breaks far better than regular polish, so you can explore tide pools, hike, and adventure without worrying about your manicure. That said, maybe skip the tide pools with a fresh set of stiletto extensions!",
      "Get adventure-ready nails at The Nail Ladie, then explore the coast. Book at vagaro.com/thenailladie."]),

    ("Private Salon Experience: Why One-on-One Matters", "private-salon-experience-one-on-one",
     "The benefits of a private, one-on-one nail salon. Why The Nail Ladie in Depoe Bay offers a completely different experience.",
     "private nail salon", "about",
     ["Walk into a typical nail salon and you'll find rows of stations, multiple technicians, walk-in crowds, TV noise, and a rushed atmosphere. Walk into The Nail Ladie in Depoe Bay, and it's just you and Heather. That difference changes everything.",
      "A private, one-on-one salon means undivided attention. Heather isn't splitting her focus between multiple clients. She's not rushing to finish your nails so the next person can sit down. Your appointment is her entire focus — and you can feel that difference in the quality of work.",
      "It also means a more relaxing experience. No competing conversations, no salon noise, no stranger sitting inches away. Just quiet music, coastal vibes, and the sound of Heather's expert work. Many clients say it feels more like visiting a friend than going to a salon.",
      "The one-on-one model also means better hygiene and sanitation. With only one client at a time, tools and surfaces are thoroughly sanitized between every appointment. There's no cross-contamination risk from adjacent stations.",
      "Experience the difference at The Nail Ladie. Book your private salon appointment at vagaro.com/thenailladie or call (541) 992-1887."]),

    ("Haircuts at The Nail Ladie: Not Just Nails", "haircuts-at-the-nail-ladie-depoe-bay",
     "The Nail Ladie in Depoe Bay also offers haircuts. Women's, men's, and children's cuts, bang trims, and blowouts.",
     "haircuts Depoe Bay", "services",
     ["The Nail Ladie isn't just about nails and lashes — we also offer haircuts! At 531 US-101 in Depoe Bay, Heather provides quality cuts for women, men, and kids in the same private, one-on-one setting that makes our nail services special.",
      "Our haircut menu includes: standard haircut ($35) for a precision cut with consultation, haircut upgrade ($50) for more detailed styling and technique, buzz cut ($20) for a clean, classic men's style, and neck/bang trim ($15) for a quick refresh between full cuts.",
      "Add-on blowout services are available too. A quick 15-minute blowout is $15, perfect for a polish after your cut. For a more styled, voluminous blowout, the 30-minute option is $35. Both can be added to any haircut or booked as standalone services.",
      "The one-on-one salon experience works beautifully for haircuts. Heather takes time to consult on your desired style, assess your hair type and face shape, and deliver a cut that you'll love. No rush, no assembly line — just a great haircut.",
      "Combine a haircut with a manicure or lash service for a full beauty refresh. Book at vagaro.com/thenailladie or call (541) 992-1887."]),

    ("Seint Makeup Artistry at The Nail Ladie", "seint-makeup-artistry-depoe-bay",
     "Seint Beauty makeup artistry and custom color matching at The Nail Ladie in Depoe Bay. Find your perfect foundation and contour shades.",
     "Seint makeup", "services",
     ["Looking for natural, beautiful makeup that enhances your features? The Nail Ladie in Depoe Bay is proud to be a Seint Beauty artist, offering custom color matching and makeup application in our private salon.",
      "Seint Beauty uses a unique IIID (cream) foundation system that simplifies your makeup routine. Instead of multiple products — foundation, concealer, contour, bronzer, blush, highlight — Seint uses cream colors that blend seamlessly together for a natural, skin-like finish.",
      "At The Nail Ladie, Heather offers free color matching. Send a selfie in natural light and she'll match your perfect Seint shades via text — no appointment needed for the color match itself. If you'd like an in-person application lesson, she can show you exactly how to apply your custom palette.",
      "Seint makeup is perfect for Oregon Coast living. The cream formula works with (not against) natural skin texture and doesn't cake or flake in ocean air and humidity. It's buildable, blendable, and lasts all day.",
      "Interested in Seint Beauty? Contact The Nail Ladie at (541) 992-1887 or book at vagaro.com/thenailladie."]),

    # 81-95: More educational + service combos
    ("Nail Extensions: Full Guide to Gel-X and Hard Gel", "nail-extensions-full-guide-gel-x-hard-gel",
     "Complete guide to nail extensions at The Nail Ladie in Depoe Bay. Gel-X tips, sculpted hard gel, lengths, shapes, and pricing.",
     "nail extensions guide", "educational",
     ["Nail extensions are the fastest way to transform short or bitten nails into the long, gorgeous nails you've always wanted. At The Nail Ladie in Depoe Bay, we offer two professional extension systems — and this guide covers everything you need to know.",
      "Gel-X Extensions ($110): Pre-formed soft gel tips bonded to your natural nails with adhesive gel. Pros: lightweight, natural feel, wide shape selection, easier removal. Ideal for: first-time extension clients, those who want a comfortable, natural feel.",
      "Sculpted Hard Gel Extensions ($110): Custom-built extensions created from hard gel using a nail form. Heather sculpts each nail by hand to your exact specifications. Pros: completely custom, very durable, thinner profile. Ideal for: clients who want a precise, custom fit and maximum durability.",
      "Both systems support lengths from Level 1 (short/active) to Level 4 (extra-long, +$35) and all shapes including specialty options like coffin, almond, and stiletto ($15 upgrade). Both are compatible with all nail art, chrome, and stamping.",
      "Extensions require fills every 2-3 weeks ($70-$90 depending on timing). With regular maintenance, you can wear extensions indefinitely. Book a consultation at vagaro.com/thenailladie to discuss which system is right for you."]),

    ("Pedicure Guide: Which Pedicure Service Is Right for You?", "pedicure-guide-which-service-right",
     "Choosing the right pedicure at The Nail Ladie in Depoe Bay. Petite vs Classic, gel vs regular polish. Complete pedicure guide.",
     "pedicure guide", "educational",
     ["At The Nail Ladie in Depoe Bay, we offer several pedicure options to fit different needs and budgets. Here's how to choose the right one for you.",
      "Petite Pedicure ($35): A maintenance-focused service that includes nail shaping, cuticle care, light callus work, and regular polish application. Takes about 30-35 minutes. Perfect for regular upkeep or when you're short on time. Add gel polish for $60 total.",
      "Classic Pedicure ($70): The full spa experience. Includes everything in the petite plus extended soaking, thorough callus removal, exfoliating sugar scrub, and a luxurious foot and lower leg massage. Takes about 50-60 minutes. Add gel polish for $85 total.",
      "Gel-Polish Pedicure ($35): A standalone gel polish application on already-maintained toenails. If you do regular pedicures and just need a color change or refresh between full services, this is your pick.",
      "Add-ons: Extra Care (+$15) for additional attention to problem areas, Hot Stone Massage (+$15) for therapeutic warm basalt stone massage with your classic pedicure. Book at vagaro.com/thenailladie."]),

    ("Nail Art Tiers Explained: Simple to Custom", "nail-art-tiers-explained-pricing",
     "Understanding nail art pricing tiers at The Nail Ladie in Depoe Bay. What you get at each level from Simple ($15) to Custom ($60).",
     "nail art pricing", "educational",
     ["At The Nail Ladie in Depoe Bay, nail art is organized into four tiers based on complexity, time, and technique. Here's exactly what you can expect at each level — so you can choose the right option for your budget and style goals.",
      "Tier 1 — Simple ($15): Single-technique accent designs. Examples: basic stamping on 1-2 nails, simple glitter fade on tips, single color French tips, a few rhinestones, minimal line art. Quick to apply, effective impact.",
      "Tier 2 — Medium ($25): Multi-element designs with more detail. Examples: full-hand stamping, two-color ombre, detailed French variations, patterned accent nails, dot art, more intricate line work. This tier covers most popular Instagram-style nail art.",
      "Tier 3 — Advanced ($50): Multi-technique, multi-color designs requiring significant skill and time. Examples: layered stamping with multiple colors, hand-painted florals combined with chrome, 3D elements, elaborate geometric patterns, landscape-inspired art.",
      "Tier 4 — Custom ($60): Anything goes. Fully custom, one-of-a-kind designs. You bring the vision, Heather makes it reality. Character art, photo-realistic designs, intricate themed sets, multi-technique masterpieces. This tier is wearable art. Book at vagaro.com/thenailladie."]),

    ("Gel-Polish Removal: Why Professional Matters", "gel-polish-removal-professional-matters",
     "Why you should always get gel polish professionally removed. The Nail Ladie in Depoe Bay explains the importance of proper gel removal.",
     "gel polish removal", "educational",
     ["We get it — you're ready for a new color and you're tempted to peel off your gel polish at home. But at The Nail Ladie in Depoe Bay, we've seen the damage that DIY gel removal causes, and we strongly recommend professional removal every time.",
      "When you peel gel polish, you're not just removing the gel — you're ripping off the top layers of your natural nail along with it. This thins and weakens your nails, creates rough texture, and can take months to grow out. One peeling session can undo weeks of healthy nail growth.",
      "Professional gel removal at The Nail Ladie is $15 and takes about 10-15 minutes. We use acetone wraps that dissolve the gel bond without affecting your natural nail. The gel slides off cleanly, leaving your natural nail smooth and intact underneath.",
      "Even better: when you book a new gel service, removal of the previous gel is included. So if you're coming in for a fresh manicure, there's no extra charge for removing your old gel. Heather will remove, prep, and reapply in one seamless appointment.",
      "Keep your nails healthy — always get gel professionally removed. Book at vagaro.com/thenailladie or call (541) 992-1887."]),

    ("New Client Guide: Your First Visit to The Nail Ladie", "new-client-guide-first-visit-nail-ladie",
     "First time visiting The Nail Ladie in Depoe Bay? Here's everything you need to know about your first appointment.",
     "new client guide", "about",
     ["Welcome! If you're booking your first appointment at The Nail Ladie in Depoe Bay, here's everything you need to know to make your visit smooth and enjoyable.",
      "Booking: The easiest way to book is online at vagaro.com/thenailladie. You can see available time slots, choose your service, and book 24/7. You can also call (541) 992-1887 during business hours (Wednesday-Saturday, 8 AM - 6:45 PM).",
      "When you arrive: Our salon is at 531 US-101 Suites K1-2 in Depoe Bay, right on Highway 101. Free parking is available right out front. Come in and Heather will welcome you to the private studio. There's no waiting room chaos — you're the only client.",
      "What to expect: Heather will start with a brief consultation about your nail goals, preferences, and any concerns. If you're getting nail extensions and coming from another technician, there's a small new client fill add-on ($15) to ensure proper product compatibility. Regular services have no new client fees.",
      "What to bring: photos of nail designs you love (Pinterest, Instagram), ideas about shape and length preferences, and an open mind! Heather will guide you through every decision. Follow @the_nail_ladie on Instagram for design inspiration before your visit. Book at vagaro.com/thenailladie."]),

    ("Gift Ideas: Beauty Gift Guide from The Nail Ladie", "beauty-gift-guide-nail-ladie-depoe-bay",
     "Gift a beauty experience at The Nail Ladie in Depoe Bay. Gift certificates, service ideas, and packages for any occasion.",
     "beauty gift ideas", "lifestyle",
     ["Looking for the perfect gift? A beauty experience at The Nail Ladie in Depoe Bay is a gift that's always appreciated, always the right size, and never needs returning. Here are our top gift ideas for any occasion.",
      "For birthdays: a gel manicure ($35) is a universally loved treat. Upgrade to structured gel ($65) or extensions ($110) for something extra special. Add nail art for a truly memorable birthday experience.",
      "For holidays: a Classic Pedicure with Gel Polish ($85) is the ultimate stocking stuffer for self-care lovers. Or gift a combo manicure-pedicure experience for an extended pampering session.",
      "For brides and bridesmaids: offer to cover the wedding party's nail appointments. Gel manicures with bridal nail art make a meaningful and practical bridal party gift.",
      "Gift certificates are available for any dollar amount or specific service. Call The Nail Ladie at (541) 992-1887 to purchase. The certificate can be physical or digital — perfect for long-distance gifting to someone on the Oregon Coast. Book at vagaro.com/thenailladie."]),

    # 86-100: More topics
    ("Nail Salon Hygiene: How The Nail Ladie Keeps You Safe", "nail-salon-hygiene-safety-standards",
     "Hygiene and sanitation practices at The Nail Ladie in Depoe Bay. How our private salon keeps you safe.",
     "nail salon hygiene", "about",
     ["Salon hygiene is a serious concern — and it should be. At The Nail Ladie in Depoe Bay, our private one-on-one salon model offers hygiene advantages that traditional multi-station salons simply cannot match.",
      "Single client, complete sanitation: Because Heather works with one client at a time, every tool and surface is thoroughly cleaned and sanitized between appointments. There's no risk of cross-contamination from adjacent workstations or shared spaces.",
      "Professional-grade tools: All metal tools are cleaned, disinfected, and sterilized according to Oregon Board of Cosmetology standards. Single-use items like files, buffers, and wooden sticks are used once and discarded. We never reuse disposable items.",
      "Clean product handling: Gel, dip powder, and other products are dispensed carefully to prevent cross-contamination. We follow strict protocols for product hygiene that go beyond state requirements.",
      "Your health matters to us. If you have any concerns about salon hygiene or want to know more about our practices, Heather is happy to walk you through our procedures. Book with confidence at vagaro.com/thenailladie."]),

    ("Nail Salon Etiquette: Tips for a Great Experience", "nail-salon-etiquette-tips",
     "Nail salon etiquette guide from The Nail Ladie in Depoe Bay. How to get the most out of your nail appointment.",
     "nail salon etiquette", "educational",
     ["Whether it's your first salon visit or your hundredth, these etiquette tips will help you get the most out of your appointment at The Nail Ladie in Depoe Bay.",
      "Be on time: Our one-on-one scheduling means your appointment is reserved just for you. Arriving late means less time for your service. If you're running late, a quick text or call lets Heather adjust. If you need to cancel, 24 hours notice is appreciated.",
      "Know what you want (or be open to suggestions): It's great to come with Pinterest or Instagram photos for inspiration. But if you're not sure, that's totally fine too — Heather loves helping clients discover new styles. The consultation at the beginning of your appointment is the perfect time to explore options.",
      "Communicate: If something doesn't feel right during your appointment — pressure, temperature, shape — speak up! Heather wants you to be completely happy with the result. It's much easier to adjust during the service than after.",
      "Phone etiquette: Feel free to use your phone during your appointment — scroll Instagram, listen to a podcast, respond to texts. Just avoid phone calls during the service, as movement can affect the precision of nail work. Book your appointment at vagaro.com/thenailladie."]),

    ("Why Choose a Solo Nail Technician Over a Big Salon", "solo-nail-technician-vs-big-salon",
     "Benefits of choosing a solo nail technician like The Nail Ladie in Depoe Bay over a large chain nail salon.",
     "solo nail technician", "about",
     ["Big box nail salons have their place — but if quality, consistency, and personalized service matter to you, a solo nail technician like Heather at The Nail Ladie in Depoe Bay is the better choice. Here's why.",
      "Consistency: At a big salon, you might get a different technician every visit. Each has different skills, habits, and attention to detail. At The Nail Ladie, it's always Heather. She knows your nail history, your preferences, your trouble spots. Every visit builds on the last.",
      "Skill depth: Solo technicians often have deeper specialization than salon employees. Heather has spent 18 years developing expertise in gel, extensions, stamping, chrome, lash extensions, and more. In a big salon, technicians often do basic services only.",
      "Time and attention: Big salons optimize for volume — more clients per hour means more revenue. A solo technician optimizes for quality. Heather takes the time needed to get every detail right. No rushing, no shortcuts, no compromise.",
      "Relationship: Over time, you build a real relationship with your solo technician. She becomes your trusted beauty advisor — someone who knows what works for you and isn't afraid to steer you toward (or away from) a particular choice. Book at vagaro.com/thenailladie."]),

    ("How to Book an Appointment at The Nail Ladie", "how-to-book-appointment-nail-ladie",
     "Step-by-step guide to booking your appointment at The Nail Ladie in Depoe Bay, Oregon. Online and phone booking options.",
     "book appointment", "about",
     ["Booking an appointment at The Nail Ladie in Depoe Bay is quick and easy. Here's how to secure your spot.",
      "Online booking (available 24/7): Visit vagaro.com/thenailladie. Browse available services, select your preferred date and time, and confirm your booking. You'll receive a confirmation email with your appointment details. The Vagaro system lets you book, reschedule, and manage your appointments anytime.",
      "Phone booking: Call (541) 992-1887 during business hours (Wednesday-Saturday, 8 AM - 6:45 PM). Heather will help you choose the right service and find a time that works for your schedule.",
      "Walk-ins: Walk-ins are welcome when availability allows. However, since The Nail Ladie is a one-chair salon, walk-in availability is limited. We strongly recommend booking ahead, especially during weekends and holidays.",
      "Cancellation policy: Please give at least 24 hours notice if you need to cancel or reschedule. This allows other clients the opportunity to book the open slot. Book today at vagaro.com/thenailladie!"]),

    ("Nail Polish Color Trends for Every Season", "nail-polish-color-trends-every-season",
     "Seasonal nail polish color guide from The Nail Ladie in Depoe Bay. The best colors for spring, summer, fall, and winter.",
     "nail color trends", "trends",
     ["Not sure what color to get? The Nail Ladie in Depoe Bay has you covered with this seasonal nail color guide. Whether you follow trends or prefer timeless choices, here's what's looking gorgeous every season.",
      "Spring: Pastels reign — lavender, baby pink, mint green, butter yellow, periwinkle. Coral and peach are universally flattering spring choices. Sheer and milky shades give a fresh, dewy look.",
      "Summer: Go bold! Bright orange, hot pink, electric blue, vibrant red, and neon shades pop against tanned skin. Classic white nails are a summer staple. Ocean-inspired teal and seafoam are perfect for coastal living.",
      "Fall: Warm, rich tones — burgundy, forest green, burnt orange, chocolate brown, mustard, and plum. These earth tones complement fall fashion and foliage perfectly. Matte finishes add extra autumnal sophistication.",
      "Winter: Deep, dramatic shades — black, navy, oxblood, emerald, and deep plum. Holiday sparkle with gold, silver, and champagne glitter. Classic red is always festive. Chrome in any metallic shade adds glamour. Book at vagaro.com/thenailladie."]),

    ("Nail Shapes for Different Hand Types", "nail-shapes-for-different-hand-types",
     "Which nail shape flatters your hand type? Expert guide from The Nail Ladie in Depoe Bay on choosing the most flattering shape.",
     "nail shapes hand types", "educational",
     ["Different nail shapes flatter different hand types. At The Nail Ladie in Depoe Bay, Heather helps every client find the most flattering shape for their unique hands. Here's a quick guide.",
      "Wide nail beds: Oval and almond shapes create the illusion of narrower, more elongated nails. Avoid square shapes, which can make wide nails look even wider. Round is a safe classic choice.",
      "Narrow nail beds: Square and squoval shapes add width and balance to narrow nails. Coffin (ballerina) shape also works well, adding visual weight at the tip. Avoid very pointed shapes like stiletto, which can make narrow nails look even thinner.",
      "Short fingers: Oval and almond shapes elongate the fingers visually. Keep nails at a moderate length — too long can look disproportionate, but a bit of length adds elegance. Nude and dark colors also help elongate.",
      "Long fingers: Lucky you — most shapes work well! Square and coffin shapes look particularly striking on long fingers. You can also pull off bolder lengths without it looking overwhelming. Experiment and have fun with shape. Heather will guide you at your appointment. Book at vagaro.com/thenailladie."]),

    # 91-100: More misc
    ("Oregon Coast Weather and Your Nails: What to Know", "oregon-coast-weather-nail-care",
     "How Oregon Coast weather affects your nails and which nail services hold up best. Tips from The Nail Ladie in Depoe Bay.",
     "Oregon Coast weather nails", "educational",
     ["Living on or visiting the Oregon Coast means dealing with rain, salt air, wind, and temperature swings. Here's how coastal weather affects your nails and which services hold up best.",
      "Humidity and rain: Constant moisture exposure can cause regular polish to peel and chip quickly. Gel polish is the clear winner for coastal living — its sealed, cured surface resists moisture penetration. Structured gel and hard gel overlays add even more weather resistance.",
      "Salt air: Saltwater and salt spray can dry out cuticles and make nails brittle over time. Counter this with daily cuticle oil application. At The Nail Ladie, we recommend jojoba-based cuticle oils that create a moisture barrier against salt air.",
      "Temperature swings: Oregon Coast temperatures can swing 20+ degrees in a day. Nail products expand and contract with temperature changes, which can stress the bond. Gel and structured gel handle temperature fluctuations better than dip powder or regular polish.",
      "Bottom line: gel-based services are ideal for Oregon Coast living. They resist moisture, handle temperature changes, and maintain their shine through whatever the coast throws at them. Book your weather-proof nails at vagaro.com/thenailladie."]),

    ("5 Star Reviews: What Clients Say About The Nail Ladie", "five-star-reviews-nail-ladie-depoe-bay",
     "Read what clients say about The Nail Ladie in Depoe Bay. 5-star reviews and testimonials from Oregon Coast nail salon customers.",
     "nail salon reviews", "about",
     ["At The Nail Ladie in Depoe Bay, we're proud of our 5-star rating. But don't take our word for it — here's what our clients have to say about their experience.",
      "Clients consistently praise three things: the quality of Heather's work, the relaxing one-on-one atmosphere, and the personalized attention that you simply can't get at a bigger salon. Many clients drive from Portland, Salem, Eugene, and across the Oregon Coast specifically for The Nail Ladie.",
      "What stands out in our reviews is the longevity of the work. Clients report gel manicures lasting 3+ weeks without a single chip, extensions that feel natural and comfortable, and lash sets that maintain their fullness for weeks. Quality products plus expert application equals lasting results.",
      "The private salon experience is another frequent highlight. Clients describe the atmosphere as peaceful, welcoming, and luxurious — a true escape from everyday stress. Many say it feels less like a salon appointment and more like visiting a talented friend.",
      "Experience the 5-star difference yourself. Book at vagaro.com/thenailladie or call (541) 992-1887. Check our reviews on Facebook and Vagaro."]),

    ("Why Depoe Bay Is the Perfect Location for a Nail Salon", "why-depoe-bay-perfect-nail-salon-location",
     "Why Depoe Bay, Oregon is the ideal location for The Nail Ladie. Coastal charm, tourism, and community.",
     "Depoe Bay nail salon location", "about",
     ["When Heather chose Depoe Bay for The Nail Ladie, it wasn't just about finding a space — it was about finding a home. Depoe Bay, Oregon, is the perfect location for a boutique nail salon, and here's why.",
      "Charm and character: Depoe Bay is one of the most charming small towns on the Oregon Coast. With its historic bridge, tiny harbor, whale watching culture, and tight-knit community, it's a place where a small business can thrive on personal connections and word-of-mouth reputation.",
      "Central location: Situated between Lincoln City and Newport on Highway 101, Depoe Bay draws visitors and residents from across the Central Oregon Coast. It's an easy day-trip destination for anyone living within an hour's drive.",
      "Tourism: Depoe Bay attracts tourists year-round — whale watchers, storm watchers, beach lovers, and road trippers. The Nail Ladie welcomes visitors who want a beauty refresh during their Oregon Coast vacation. Walk-ins and advance bookings are both available.",
      "Community: Above all, Depoe Bay is a community that supports small businesses. The Nail Ladie is proud to be part of the Depoe Bay business family. Book at vagaro.com/thenailladie."]),

    ("Nail Care for Active Oregon Coast Women", "nail-care-active-oregon-coast-women",
     "Nail tips for active, outdoor-loving Oregon Coast women. Durable nail services that keep up with your lifestyle from The Nail Ladie.",
     "nail care active lifestyle", "lifestyle",
     ["Oregon Coast women aren't sitting still. You're hiking, kayaking, tide pooling, gardening, surfing, and exploring. Your nails need to keep up with your active lifestyle — and at The Nail Ladie in Depoe Bay, Heather designs manicures that are as durable as they are beautiful.",
      "Best services for active lifestyles: Structured gel manicure ($65) adds a reinforcing layer over your natural nails — strong enough for any activity. Gel-polish manicure ($35) offers chip-resistant color that handles whatever your day brings. Short-to-medium nail lengths with round or oval shapes offer the best durability for active hands.",
      "If you love extensions but worry about breakage, talk to Heather about a durable, shorter set. Active-length Gel-X or hard gel extensions offer beauty without the breakage risk of extra-long nails. Strong shape choices like round or squoval reduce catching and snagging.",
      "Daily habits that protect active nails: wear gardening gloves (always!), use sunscreen on your hands to prevent gel discoloration, rinse salt water off after beach activities, and apply cuticle oil after exposure to chlorine, salt water, or cleaning products.",
      "Get adventure-ready nails at The Nail Ladie. Book at vagaro.com/thenailladie or call (541) 992-1887."]),

    ("Instagram-Worthy Nails at The Nail Ladie", "instagram-worthy-nails-nail-ladie",
     "Want nails that break the internet? The Nail Ladie in Depoe Bay creates Instagram-worthy nail art. Follow @the_nail_ladie for inspiration.",
     "Instagram nails", "lifestyle",
     ["Want nails that make people stop scrolling? At The Nail Ladie in Depoe Bay, Heather creates Instagram-worthy nail designs that are as photogenic as they are wearable. Follow @the_nail_ladie for daily inspiration.",
      "What makes nails Instagram-worthy? It's the combination of flawless application, creative design, and perfect photography conditions. Heather's attention to detail — clean cuticle work, even coating, crisp nail art lines — creates nails that photograph beautifully from every angle.",
      "Our most-liked Instagram designs include chrome mirror nails in rose gold, galaxy-inspired cat eye in deep blue, intricate floral stamping on nude bases, glitter ombre fades, and custom character/themed nail art. Each set is one-of-a-kind.",
      "Pro photo tip: natural light is your best friend for nail photos. After your appointment, step outside The Nail Ladie and use the natural Oregon coastal light to photograph your fresh nails. The ocean or Depoe Bay Bridge make a gorgeous backdrop.",
      "Tag @the_nail_ladie in your nail photos and we may share your post! Book your Instagram-worthy set at vagaro.com/thenailladie."]),

    # 96-111: Final batch
    ("Nail Salon vs DIY: Why Professional Nails Are Worth It", "nail-salon-vs-diy-professional-worth-it",
     "Professional nail salon vs DIY home manicure. Why investing in professional nails at The Nail Ladie in Depoe Bay pays off.",
     "professional nails vs DIY", "comparison",
     ["With nail polish and tools available at every drugstore, it's tempting to do your nails at home. But here's why a professional gel manicure at The Nail Ladie in Depoe Bay is worth the investment.",
      "Longevity: A home manicure lasts 3-5 days before chipping. A professional gel manicure lasts 2-3 weeks — roughly 5x longer. When you factor in the time spent repainting every few days, professional nails actually save you time over the month.",
      "Finish quality: Even the steadiest hand can't match the even, flawless application of a trained professional. Heather applies gel in thin, perfectly even coats with no brushstrokes, bubbles, or flooding. The finish is mirror-smooth.",
      "Nail health: Professional manicures include proper cuticle care, nail shaping, and assessment of nail health. Many nail problems — thinning, peeling, ridges — can be addressed or prevented with regular professional care. Improper home techniques can actually damage nails.",
      "The experience: let's be real — painting your own nails is a chore. Getting your nails done at The Nail Ladie is a treat. Relax in a private salon, let a professional handle the work, and walk out feeling pampered. From $35 at vagaro.com/thenailladie."]),

    ("Oregon Coast Gift Experience: Nails, Lashes, and the Coast", "oregon-coast-gift-experience-beauty",
     "Give the gift of an Oregon Coast experience — nails at The Nail Ladie, whale watching, dining in Depoe Bay. The ultimate gift package idea.",
     "Oregon Coast gift experience", "lifestyle",
     ["The best gifts aren't things — they're experiences. Here's how to gift someone a perfect day on the Oregon Coast, starting with a pampering session at The Nail Ladie in Depoe Bay.",
      "Step 1: Book a nail and/or lash appointment at The Nail Ladie (call (541) 992-1887 for gift certificates). A gel manicure and pedicure combo makes a luxurious gift that takes about 90 minutes of pure pampering.",
      "Step 2: Add a Depoe Bay dining experience. Give a gift card to one of Depoe Bay's waterfront restaurants for a post-appointment seafood lunch with ocean views. The complete package: beauty + dining + coastal scenery.",
      "Step 3: For the ultimate experience, add a whale watching charter ticket. Several operators in Depoe Bay offer gift certificates for 1-2 hour whale watching trips. Combine all three — nails, lunch, and whales — for an unforgettable Oregon Coast day.",
      "This experience package makes a perfect birthday, Mother's Day, anniversary, or holiday gift. All you need is a phone call or two to put it together. Start with The Nail Ladie at vagaro.com/thenailladie."]),

    ("Nail Extensions for Bitten Nails: Transform Your Hands", "nail-extensions-bitten-nails-transformation",
     "Nail extensions for nail biters at The Nail Ladie in Depoe Bay. Transform bitten nails into beautiful, healthy-looking nails.",
     "nail extensions bitten nails", "educational",
     ["If you've been biting your nails and feel embarrassed about how they look, you're not alone — and there's a solution. Nail extensions at The Nail Ladie in Depoe Bay can completely transform bitten nails into beautiful, healthy-looking nails.",
      "Gel-X and sculpted hard gel extensions ($110) can be applied to even very short, bitten nails. Heather has extensive experience working with nail biters and knows exactly how to create extensions that look natural and feel comfortable, even on minimal natural nail surface.",
      "Extensions serve a dual purpose for nail biters: they look gorgeous immediately, AND they help break the biting habit. With beautiful, smooth extensions over your natural nails, you lose the urge to pick and bite. Meanwhile, your natural nails grow healthily underneath.",
      "Start with a shorter, more natural length and shape — this feels more comfortable for first-time extension wearers and former biters. As you get used to them and your natural nails strengthen underneath, you can gradually go longer if desired.",
      "No judgment, just beautiful nails. Heather has helped many clients transform bitten nails into hands they're proud to show off. Book your transformation at vagaro.com/thenailladie or call (541) 992-1887."]),

    ("Combination Appointments: Nails + Lashes + More", "combination-appointments-nails-lashes-pedicure",
     "Save time with combination appointments at The Nail Ladie in Depoe Bay. Get nails, lashes, pedicure, and more in one visit.",
     "combination appointment", "services",
     ["Why make two trips when you can do it all in one? At The Nail Ladie in Depoe Bay, you can combine multiple services into a single appointment for maximum pampering efficiency.",
      "Popular combinations include: Gel Manicure + Classic Pedicure (approximately 2 hours of pampering), Gel Manicure + Lash Lift and Tint (approximately 2 hours), Nail Extensions + Nail Art (approximately 1.5-2 hours), Full Lash Set + Gel Manicure (approximately 3 hours).",
      "Combination appointments are especially popular with clients who drive from Lincoln City, Newport, or further. Instead of making the trip twice, get everything done in one relaxing visit. Just let Heather know when you book so she can allocate enough time.",
      "To book a combination appointment, call (541) 992-1887 or book online at vagaro.com/thenailladie. Select your primary service when booking, then add a note about additional services. Heather will confirm the full appointment time.",
      "Maximize your visit to The Nail Ladie. Combine services, save trips, and leave feeling completely refreshed."]),

    ("Lower Lash Extensions: Complete Your Lash Look", "lower-lash-extensions-depoe-bay",
     "Lower lash extensions at The Nail Ladie in Depoe Bay. Complete your full lash look with lower lash enhancement for $30.",
     "lower lash extensions", "lashes",
     ["Upper lash extensions get all the attention, but lower lash extensions can complete your look by balancing your eye proportions and adding extra definition. At The Nail Ladie in Depoe Bay, lower lash extensions are available for $30 as an add-on to any upper lash service.",
      "Lower lash extensions involve applying small, fine extensions to the bottom lashes. This creates a more balanced, wide-eyed look — especially for clients with naturally sparse or light-colored lower lashes.",
      "Lower extensions are particularly effective for: clients who want a more dramatic, complete lash look; photoshoots and special events where every detail matters; clients whose lower lashes are lighter or sparser than their upper lashes.",
      "The application is similar to upper lashes but uses shorter, finer extensions. Heather takes care to apply them so they feel comfortable and don't interfere with your natural blink. Lower extensions are filled at the same appointment as your upper lash fill.",
      "Complete your lash look with lower extensions. Book at vagaro.com/thenailladie or call (541) 992-1887."]),

    ("Mini Lash Fill: Quick Lash Refresh", "mini-lash-fill-quick-refresh-depoe-bay",
     "Mini lash fill at The Nail Ladie in Depoe Bay. Quick, affordable lash refresh for $40 when you just need a touch-up.",
     "mini lash fill", "lashes",
     ["Sometimes you don't need a full fill — just a quick touch-up. The Mini Lash Fill at The Nail Ladie in Depoe Bay ($40) is designed for exactly that. It's a shorter appointment focused on filling in the most noticeable gaps without a complete fill.",
      "A mini fill is ideal when: you're between regular fills and have just a few gaps, you have a special event coming up and want a quick refresh, your retention is generally excellent and you only lose a few lashes between fills, or you want a budget-friendly option between full fills.",
      "The mini fill appointment is shorter than a standard fill — about 30-45 minutes. Heather focuses on the areas where lash loss is most visible (usually the outer corners and center), bringing your set back to fullness without the time commitment of a full fill.",
      "Important note: mini fills work best when you're maintaining a regular fill schedule. If you've lost more than 40-50 percent of your extensions, a full fill or new full set may be recommended instead.",
      "Quick lash refresh when you need it. Book a mini fill at vagaro.com/thenailladie or call (541) 992-1887."]),

    ("Specialty Nail Shapes: Coffin, Almond, and Stiletto", "specialty-nail-shapes-coffin-almond-stiletto",
     "Specialty nail shapes at The Nail Ladie in Depoe Bay. Coffin, almond, and stiletto shapes for $15 upgrade. Which shape suits you?",
     "coffin almond stiletto nails", "trends",
     ["Ready to go beyond the basics? At The Nail Ladie in Depoe Bay, specialty nail shapes — coffin (ballerina), almond, and stiletto — are available as a $15 upgrade on any manicure or extension service. Here's the lowdown on each.",
      "Coffin (Ballerina): Named for its resemblance to a coffin shape (or a ballerina's pointe shoe), coffin nails are long with tapered sides and a flat, squared-off tip. This shape is the most popular specialty shape and looks especially stunning with ombre, chrome, and glitter designs.",
      "Almond: Almond nails are filed to a soft point, mimicking the shape of an almond nut. They're elegant, feminine, and incredibly flattering — the tapered shape elongates the fingers and makes hands look more slender. Almond nails look gorgeous with any nail art style.",
      "Stiletto: The most dramatic shape, stiletto nails come to a sharp, dramatic point. They make a bold fashion statement and are a favorite for special occasions, editorial looks, and anyone who loves to stand out. Note: stilettos require medium to long length to achieve the shape.",
      "All specialty shapes work on both natural nails (at sufficient length) and extensions. Heather will help you choose the shape that best suits your lifestyle, hand shape, and style goals. Book at vagaro.com/thenailladie."]),

    ("Color Lash Extensions: Add a Pop of Color", "color-lash-extensions-depoe-bay",
     "Color lash extensions at The Nail Ladie in Depoe Bay. Add pops of colored lash extensions for $15. Blue, purple, green, and more.",
     "color lash extensions", "lashes",
     ["Why stick to black when you can add a pop of color? Color lash extensions at The Nail Ladie in Depoe Bay are a fun, unique way to customize your lash look. Add color for just $15 on top of any lash service.",
      "Color lash extensions use synthetic fibers in non-natural shades — blue, purple, teal, green, burgundy, and more. They can be applied as a full set of color (bold and eye-catching), as accent lashes mixed into a black base (subtle pops of color), or concentrated in the outer corners for a graduated color effect.",
      "Popular color choices: deep blue enhances brown eyes, purple and plum complement hazel and green eyes, teal is bold and playful on any eye color, and burgundy adds warmth and richness. Heather will recommend colors that complement your eye color and personal style.",
      "Color lashes are especially popular for music festivals, pride celebrations, themed parties, holiday looks, and anyone who loves expressing their individuality. They're also a fun seasonal option — teal for summer, burgundy for fall, emerald for the holidays.",
      "Add color to your lash look. Book at vagaro.com/thenailladie or call (541) 992-1887."]),

    ("Custom Lash Styling: Find Your Signature Look", "custom-lash-styling-signature-look",
     "Custom lash styling at The Nail Ladie in Depoe Bay. Eye shape analysis and personalized lash design for your unique features.",
     "custom lash styling", "lashes",
     ["Not all eyes are the same, so not all lash sets should be the same. At The Nail Ladie in Depoe Bay, custom lash styling ($15 add-on) includes eye shape analysis and a personalized lash design crafted specifically for your unique features.",
      "Eye shapes and their ideal lash styles: Almond eyes (the most versatile) look great with virtually any style. Round eyes benefit from cat-eye styling (longer extensions on the outer corners) to elongate. Hooded eyes look best with curly, lifted lashes that peek over the lid. Downturned eyes benefit from outer corner lifts. Close-set eyes are opened up with longer lashes in the center and outer corners.",
      "Beyond eye shape, Heather considers your facial proportions, brow shape, personal style, and lifestyle when designing your lash set. Someone who wears glasses needs a different curl and length than someone who doesn't. Someone who wants a natural look gets a different mapping than someone who wants full glam.",
      "The custom styling add-on includes a thorough eye consultation, a personalized lash map (determining length, curl, and volume across the lash line), and application following the custom design.",
      "Find your signature lash look at The Nail Ladie. Book at vagaro.com/thenailladie."]),

    ("New Technician Fill Add-On: Switching to The Nail Ladie", "new-technician-fill-switching-salons",
     "Switching nail salons? The Nail Ladie in Depoe Bay offers a new technician fill add-on for $15 to ensure a seamless transition.",
     "switching nail salons", "services",
     ["Switching to a new nail technician? Welcome to The Nail Ladie in Depoe Bay! We're glad you're here. If you're coming in with existing nail extensions from another salon, here's what you need to know.",
      "Our New Client Fill add-on ($15) covers the extra time and assessment needed when working with extensions applied by a different technician. Every technician uses slightly different products, techniques, and application methods. Heather needs to evaluate your current extensions to determine the best approach for maintenance.",
      "During your first fill, Heather will assess the product type and condition of your current extensions, check for lifting, damage, or product compatibility issues, determine whether a fill, rebalance, or removal and new set is the best path forward, and establish a maintenance plan going forward.",
      "In most cases, Heather can work with your existing extensions seamlessly. If the product or application isn't compatible with our system, she'll let you know and recommend the best course of action — which might mean soaking off and starting fresh with a new full set.",
      "Switching salons doesn't have to be stressful. Book your first appointment at vagaro.com/thenailladie or call (541) 992-1887."]),

    ("Nail Repair: Quick Fixes for Broken or Damaged Nails", "nail-repair-broken-damaged-nails",
     "Broke a nail? The Nail Ladie in Depoe Bay offers quick nail repairs for $15 per nail. Fix breaks, cracks, and chips fast.",
     "nail repair", "services",
     ["Broke a nail? Cracked a gel coat? At The Nail Ladie in Depoe Bay, individual nail repairs are $15 per nail and can usually be done as a quick drop-in or added to your next scheduled appointment.",
      "Common nail repairs include: fixing a cracked or broken natural nail with a reinforcing gel patch, reattaching or replacing a single loose or popped-off extension, filling a chip or dent in gel or hard gel, and repairing lifting at the cuticle area.",
      "A single nail repair takes about 10-15 minutes. If you break a nail between appointments, call (541) 992-1887 and Heather will try to fit you in the same day or next available slot. Don't try to fix it at home with super glue — that can trap moisture and cause bigger problems.",
      "Prevention tips: avoid using your nails as tools (opening cans, picking labels, scratching surfaces), wear gloves for heavy-duty tasks, and keep nails at a manageable length for your lifestyle. If you're consistently breaking a specific nail, Heather can add extra reinforcement to that nail at your next appointment.",
      "Quick repairs, expert care. Book at vagaro.com/thenailladie."]),

    ("French Ombre (Baby Boomer) Nails Guide", "french-ombre-baby-boomer-nails",
     "French ombre baby boomer nails at The Nail Ladie in Depoe Bay. The soft, blended alternative to traditional French tips.",
     "French ombre nails", "trends",
     ["French ombre — also called baby boomer nails — is a modern, softer take on the classic French manicure. Instead of a sharp white tip line, the white gradually blends into a nude or pink base, creating a beautiful gradient effect.",
      "At The Nail Ladie in Depoe Bay, French ombre is available as a French-Design add-on ($15) on any manicure or extension service. Heather uses a sponge technique to blend the white and nude colors seamlessly — the transition is so smooth it looks like a natural gradient.",
      "French ombre is one of the most universally flattering nail designs. It works on any nail shape, any length, and any skin tone. The soft gradient elongates the fingers and creates an elegant, polished look that's appropriate for any occasion.",
      "Variations on French ombre include: colored ombre (swap white for any light shade), glitter ombre (blend glitter into the white gradient), chrome ombre (add chrome powder for a metallic gradient), and reverse ombre (white at the base, nude at the tip).",
      "Get beautiful French ombre nails at The Nail Ladie. Book at vagaro.com/thenailladie."]),

    ("Consultation Services at The Nail Ladie", "consultation-services-nail-ladie-depoe-bay",
     "Nail consultation at The Nail Ladie in Depoe Bay. $15 consultation for complex designs, extension options, or nail health assessment.",
     "nail consultation", "services",
     ["Not sure what you want? Need expert advice on the best service for your nails? At The Nail Ladie in Depoe Bay, a dedicated consultation ($15) gives you Heather's professional assessment and recommendation — without committing to a service.",
      "Consultations are perfect for: first-time extension clients who want to discuss Gel-X vs hard gel, clients with nail damage who need advice on the best repair approach, complex nail art ideas that need planning and design discussion, clients switching from another salon who want to discuss their current nails, and anyone who just wants expert guidance on nail care.",
      "During a consultation, Heather will examine your natural nails, discuss your goals and lifestyle, explain relevant service options with pricing, and if applicable, plan a nail art design for your next appointment.",
      "The $15 consultation fee is credited toward your service if you book on the same day. So if you decide to go ahead with a manicure or other service immediately after the consultation, the consultation is essentially free.",
      "Book a consultation at vagaro.com/thenailladie or call (541) 992-1887."]),

    ("Depoe Bay Nail Salon for Tourists and Visitors", "depoe-bay-nail-salon-tourists-visitors",
     "Visiting Depoe Bay? The Nail Ladie welcomes tourists and visitors. Quick beauty services on the Oregon Coast, walk-ins when available.",
     "Depoe Bay tourist nail salon", "tourism",
     ["Visiting Depoe Bay on vacation? Whether you're on a weekend getaway, a road trip, or a longer Oregon Coast stay, The Nail Ladie welcomes tourists and visitors with open arms. A nail appointment is the perfect way to treat yourself during your trip.",
      "We know vacation schedules are flexible, so we try to accommodate visitors whenever possible. While appointments are always recommended (book online at vagaro.com/thenailladie), walk-ins are welcome when availability allows. Call ahead at (541) 992-1887 to check same-day openings.",
      "Quick vacation-friendly services include: gel-polish manicure ($35, about 45 minutes), petite pedicure ($35, about 30 minutes), and lash lift and tint (about 60 minutes). These services give you beautiful results without taking up your whole vacation day.",
      "Our salon is right on Highway 101 — the main road through Depoe Bay — so it's easy to find and access. Free parking out front, no appointment minimum, and you'll be back to exploring the coast in under an hour.",
      "Make your Oregon Coast vacation extra special. Book at vagaro.com/thenailladie or call (541) 992-1887."]),

    ("Acrylic vs Gel Nails: Understanding the Difference", "acrylic-vs-gel-nails-difference",
     "Acrylic vs gel nails explained. The Nail Ladie in Depoe Bay breaks down the differences to help you choose the right enhancement.",
     "acrylic vs gel nails", "educational",
     ["Acrylic and gel nails are both popular nail enhancement options, but they work differently and offer different benefits. At The Nail Ladie in Depoe Bay, we specialize in gel-based systems — here's why, and how they compare to traditional acrylic.",
      "Acrylic nails are created by mixing a liquid monomer with a powder polymer, which forms a hard protective layer over your natural nail. They're strong and durable, but they can look thicker and less natural. The application involves strong chemical odors and requires more filing on the natural nail.",
      "Gel nails (including structured gel, hard gel, and Gel-X) use a gel product that's cured under LED or UV light. Gel nails are more flexible, look more natural, and are gentler on your natural nails. The application is odor-free and involves minimal filing. At The Nail Ladie, our gel enhancements start at $65 for overlays and $110 for full extensions.",
      "Why does The Nail Ladie use gel? Heather prefers gel systems because they offer better nail health outcomes, a more natural appearance, lighter weight on the nail, and easier removal. Gel technology has advanced significantly, and modern gel extensions are just as durable as acrylic while being much gentler.",
      "Curious about switching from acrylic to gel? Book an appointment at vagaro.com/thenailladie or call (541) 992-1887. Heather can safely remove your acrylics and transition you to gel."]),

    ("How to Choose a Nail Salon: Red Flags and Green Flags", "how-to-choose-nail-salon-red-green-flags",
     "How to choose a good nail salon. Red flags to watch for and green flags that mean you've found a quality salon. Guide from The Nail Ladie.",
     "how to choose nail salon", "educational",
     ["Not all nail salons are created equal. Whether you're new to an area or looking for a change, knowing what to look for (and what to avoid) can save you from a bad experience. Here's a guide from The Nail Ladie in Depoe Bay.",
      "Green flags (signs of a great salon): Licensed and certified technicians. Clean, organized workspace. Tools are visibly sanitized between clients. The technician asks about your nail history and preferences. They take their time rather than rushing. Prices are clearly posted. They use professional-grade products.",
      "Red flags (warning signs): Strong chemical odors (may indicate poor ventilation or harsh products). Dirty tools or workstations. Technicians who rush or work on multiple clients simultaneously. Extremely low prices (quality products and proper technique cost money). No consultation or questions about allergies or preferences. Drills used aggressively on natural nails.",
      "At The Nail Ladie in Depoe Bay, we check every green flag box. Heather is licensed and certified with 18 years of experience. Our one-on-one model means zero rushing, complete hygiene control, and undivided attention. We use professional-grade gel products and follow strict sanitation protocols.",
      "Experience the difference quality makes. Book at vagaro.com/thenailladie or call (541) 992-1887."]),

    ("Nail Salon Gift Certificate Ideas", "nail-salon-gift-certificate-ideas",
     "Gift certificate ideas from The Nail Ladie in Depoe Bay. The perfect gift for birthdays, holidays, Mother's Day, and any special occasion.",
     "nail salon gift certificate", "lifestyle",
     ["Stuck on what to give someone who has everything? A gift certificate to The Nail Ladie in Depoe Bay is always the right answer. It's a gift of self-care, beauty, and relaxation — something most people won't splurge on for themselves.",
      "Gift certificate suggestions by budget: $35 covers a classic or gel-polish manicure. $70 covers a classic pedicure. $85 covers a classic pedicure with gel polish or a manicure with nail art. $110 covers a full set of nail extensions. $150 covers a full set of lash extensions.",
      "Gift certificates are available in any dollar amount, so you can customize to your budget. They never expire, so the recipient can use them whenever works for their schedule. We can provide physical certificates for in-person gifting or digital ones for last-minute needs.",
      "Popular occasions for gift certificates include Mother's Day, birthdays, Valentine's Day, Christmas, anniversaries, bridal party gifts, teacher appreciation, and 'just because' treats. A beauty experience is always memorable and appreciated.",
      "Purchase a gift certificate by calling The Nail Ladie at (541) 992-1887. Questions about services? Visit vagaro.com/thenailladie."]),

    ("Nail Care During Pregnancy: What's Safe", "nail-care-during-pregnancy-safety",
     "Is it safe to get your nails done during pregnancy? The Nail Ladie in Depoe Bay answers common questions about prenatal nail care.",
     "pregnancy nail care", "educational",
     ["Expecting a baby and wondering if you can still get your nails done? The short answer is yes — with some precautions. At The Nail Ladie in Depoe Bay, Heather has experience working with pregnant clients and prioritizes their comfort and safety.",
      "Gel manicures and pedicures are generally considered safe during pregnancy. The products used at The Nail Ladie are professional-grade and applied in a well-ventilated private salon. Our gel systems don't produce the strong fumes associated with traditional acrylic nails.",
      "Pedicures are actually a wonderful treat during pregnancy. Swollen feet, aching arches, and retained water make a relaxing pedicure feel heavenly. Our Classic Pedicure ($70) includes a soothing foot soak, gentle massage, and polish. The Hot Stone Massage add-on ($15) is especially popular with expectant mothers.",
      "A few considerations: some pregnant women experience increased nail sensitivity or faster nail growth (thanks, prenatal vitamins!). Heather will adjust her technique accordingly. If you have any concerns, consult with your healthcare provider before your appointment.",
      "Treat yourself during pregnancy at The Nail Ladie. Book at vagaro.com/thenailladie or call (541) 992-1887."]),

    ("Nail Trends Through the Decades: A Style History", "nail-trends-through-decades-history",
     "From 1920s red lacquer to 2020s chrome and cat eye — a journey through nail trend history from The Nail Ladie in Depoe Bay.",
     "nail trends history", "trends",
     ["Nail art isn't a modern invention — women have been decorating their nails for thousands of years. Here's a quick journey through the decades of nail trends, from The Nail Ladie in Depoe Bay.",
      "1920s-1940s: Red nail polish became mainstream thanks to car paint technology (seriously!). Moon manicures — leaving the half-moon at the base unpainted — were the height of glamour. Deep reds and berries dominated through the war years.",
      "1950s-1970s: Pastel pinks and corals took over in the conservative 1950s. The 1960s brought bright, mod colors and square nail shapes. The 1970s introduced earth tones, French manicures debuted in the late 70s, and artificial nails became available.",
      "1980s-2000s: The 80s went bold — long, sculpted acrylic nails with neon colors and rhinestones. The 90s swung back to short, natural nails and dark grunge colors. The 2000s brought nail art mainstreaming, gel polish technology, and the rise of nail Instagram.",
      "2010s-2020s: The current era has exploded with options. Chrome, cat eye, dip powder, Gel-X extensions, stamping, ombre, and custom art are all available at The Nail Ladie. We're living in the golden age of nail art. Book at vagaro.com/thenailladie."]),

    ("Storm Watching and Nails: Winter on the Oregon Coast", "storm-watching-nails-winter-oregon-coast",
     "Combine storm watching season with a cozy nail appointment at The Nail Ladie in Depoe Bay. Winter on the Oregon Coast.",
     "storm watching nails", "tourism",
     ["Winter storm watching season is one of the best-kept secrets of the Oregon Coast. From November through March, powerful Pacific storms create dramatic waves, spectacular spray, and awe-inspiring displays of nature's power. And Depoe Bay is one of the best spots to witness it all.",
      "The combination of Depoe Bay's basalt cliffs, the Spouting Horn, and the narrow harbor channel creates some of the most dramatic storm watching on the entire coast. Waves crash against the seawall, spray erupts from the Spouting Horn, and the harbor entrance becomes a churning maelstrom.",
      "After an exhilarating morning of storm watching, warm up at The Nail Ladie. Our cozy private salon is the perfect retreat from the wild weather outside. Let Heather pamper you with a gel manicure while the rain beats against the windows. It's pure Oregon Coast winter bliss.",
      "Winter nail colors perfectly complement the moody coastal atmosphere: deep ocean blue, stormy grey, dark teal, burgundy wine, and midnight black. Add cat eye gel for an effect that mimics the churning ocean, or chrome for a metallic edge that catches the dim winter light.",
      "Plan your storm watching trip with a nail appointment at The Nail Ladie. Book at vagaro.com/thenailladie or call (541) 992-1887."]),

    ("Lash Lift vs Lash Extensions: Which Is Right for You?", "lash-lift-vs-lash-extensions-comparison",
     "Lash lift vs lash extensions — which is right for you? The Nail Ladie in Depoe Bay compares cost, maintenance, and results.",
     "lash lift vs extensions", "comparison",
     ["Lash lift or lash extensions? Both enhance your natural beauty, but they're very different treatments with different results, costs, and maintenance requirements. At The Nail Ladie in Depoe Bay, we offer both — here's how to choose.",
      "Lash lift: Uses your natural lashes. A perming solution curls them from the root, and a tint darkens them. Results last 6-8 weeks. Zero daily maintenance — no cleaning, no brushing. Perfect for active lifestyles. Best for clients with naturally long but straight lashes.",
      "Lash extensions: Synthetic fibers bonded to individual natural lashes. Dramatically adds length, volume, and definition. Results last until fill (2-3 weeks). Requires daily care — gentle cleaning, brushing, avoiding oil products. Best for clients who want a dramatic, always-glam look.",
      "Cost comparison: A lash lift is a one-time appointment with no fills needed for 6-8 weeks. Lash extensions ($150) require fills every 2-3 weeks ($75-$125). Over 8 weeks, a lash lift is significantly less expensive. However, extensions deliver a level of drama and fullness that a lift cannot match.",
      "Still not sure? Book a consultation at The Nail Ladie. Heather will assess your natural lashes and recommend the best option for your goals. Visit vagaro.com/thenailladie or call (541) 992-1887."]),

    ("Coastal-Inspired Nail Art: Oregon Coast Designs", "coastal-inspired-nail-art-oregon-coast-designs",
     "Coastal-inspired nail art at The Nail Ladie in Depoe Bay. Ocean waves, sand dollars, seashells, and Pacific Northwest nail designs.",
     "coastal nail art", "trends",
     ["Living on the Oregon Coast inspires everything — including our nail art. At The Nail Ladie in Depoe Bay, coastal-themed designs are some of our most requested looks. Here's a gallery of ocean-inspired nail art ideas.",
      "Wave nails: Gradient blues and teals that mimic the Pacific Ocean, with white-cap accents at the tips. These can be created through ombre technique, freehand painting, or stamping. Add chrome powder over the blue for a wet, ocean-surface effect.",
      "Sand dollar and seashell designs: Delicate stamped or hand-painted seashells, sand dollars, starfish, and sea urchins on nude or sandy bases. These look beautiful as accent nails paired with coastal colors like seafoam, sandy beige, or coral.",
      "Pacific Northwest nature: Think evergreen trees silhouetted against sunset skies, whale tail stamps, lighthouse designs, driftwood textures, and wave-smoothed pebble patterns. These designs celebrate the specific beauty of our Oregon Coast landscape.",
      "Get coastal nails that match your lifestyle. Book at vagaro.com/thenailladie or call (541) 992-1887. Follow @the_nail_ladie on Instagram for coastal nail art inspiration."]),
]

# ─── HTML TEMPLATE ─────────────────────────────────────────────────────────────
def blog_html(title, slug, meta_desc, body_paragraphs, keyword, category):
    body_html = ""
    for i, p in enumerate(body_paragraphs):
        if i == 0:
            body_html += f"    <p class='intro'>{p}</p>\n"
        elif i == len(body_paragraphs) - 1:
            body_html += f"    <div class='cta-box'>\n      <p>{p}</p>\n    </div>\n"
        else:
            body_html += f"    <p>{p}</p>\n"

    return f'''<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>{title} | The Nail Ladie Blog</title>
<meta name="description" content="{meta_desc}">
<meta name="robots" content="index, follow">
<link rel="canonical" href="{SITE['base']}/blog/{slug}.html">
<meta property="og:title" content="{title}">
<meta property="og:description" content="{meta_desc}">
<meta property="og:type" content="article">
<meta property="og:url" content="{SITE['base']}/blog/{slug}.html">
<script type="application/ld+json">
{{
  "@context": "https://schema.org",
  "@type": "BlogPosting",
  "headline": "{title}",
  "description": "{meta_desc}",
  "url": "{SITE['base']}/blog/{slug}.html",
  "author": {{"@type": "Person", "name": "Heather"}},
  "publisher": {{
    "@type": "Organization",
    "name": "The Nail Ladie",
    "url": "{SITE['base']}/"
  }},
  "datePublished": "2026-08-01",
  "keywords": "{keyword}, nail salon, Depoe Bay, Oregon Coast"
}}
</script>
<style>
*,*::before,*::after{{box-sizing:border-box;margin:0;padding:0}}
:root{{
  --bg:#FAF9F6;--accent:#1B6B6A;--accent-hover:#248F8D;--accent-light:#D4EEEE;
  --warm:#C4A06E;--seafoam:#5EC4C4;--ocean:#2A4F6B;--text:#1A1A1A;--text-mid:#555;
  --font-heading:Georgia,'Palatino Linotype','Book Antiqua',Palatino,'Times New Roman',serif;
  --sans:-apple-system,BlinkMacSystemFont,'Segoe UI',Roboto,'Helvetica Neue',Arial,sans-serif;
  --border:#B8D4DA;--ease:cubic-bezier(.25,.46,.45,.94);
}}
html{{scroll-behavior:smooth;overflow-x:hidden}}
body{{font-family:var(--sans);color:var(--text);background:var(--bg);line-height:1.6;-webkit-font-smoothing:antialiased}}
a{{color:var(--accent);text-decoration:none}}a:hover{{color:var(--accent-hover)}}
img{{max-width:100%;height:auto}}

.top-bar{{position:fixed;top:0;left:0;right:0;z-index:102;background:var(--accent);color:#fff;display:flex;align-items:center;justify-content:center;gap:clamp(1rem,3vw,2.5rem);padding:6px clamp(1rem,3vw,2rem);font-size:.68rem;letter-spacing:1.5px;text-transform:uppercase}}
.top-bar a{{color:#fff;display:flex;align-items:center;gap:6px;transition:color .3s}}
.top-bar a:hover{{color:var(--seafoam)}}
.top-bar svg{{width:14px;height:14px;stroke:currentColor;fill:none;stroke-width:1.5}}
.top-bar .tb-divider{{width:1px;height:12px;background:rgba(255,255,255,.25)}}

.nav{{position:fixed;top:30px;left:0;right:0;z-index:100;padding:0 clamp(1.5rem,4vw,3rem);height:80px;display:flex;align-items:center;justify-content:space-between;transition:all .5s var(--ease);background:rgba(255,255,255,.92);backdrop-filter:blur(20px);-webkit-backdrop-filter:blur(20px);box-shadow:0 2px 20px rgba(0,0,0,.08)}}
.nav.scrolled{{top:0;background:rgba(250,250,248,.95);height:64px;box-shadow:0 1px 0 var(--border)}}
.top-bar.hidden{{transform:translateY(-100%);transition:transform .3s var(--ease)}}
.nav-logo{{display:flex;align-items:center;z-index:101}}
.nav-logo-img{{height:80px;width:auto;transition:all .5s}}
.nav.scrolled .nav-logo-img{{height:50px}}
.nav-links{{display:flex;align-items:center;gap:2.5rem;list-style:none}}
.nav-links a{{font-size:.75rem;letter-spacing:1.5px;text-transform:uppercase;color:var(--text-mid);transition:color .3s;position:relative;text-decoration:none}}
.nav-links a::after{{content:'';position:absolute;bottom:-4px;left:0;width:0;height:1px;background:currentColor;transition:width .3s var(--ease)}}
.nav-links a:hover::after{{width:100%}}
.nav-book{{font-size:.7rem;letter-spacing:2px;text-transform:uppercase;padding:11px 26px;border:1px solid var(--accent);color:var(--accent);transition:all .3s var(--ease);text-decoration:none}}
.nav-book:hover{{background:var(--accent);color:#fff}}

.blog-hero{{margin-top:110px;padding:60px clamp(16px,5vw,80px) 40px;max-width:800px;margin-left:auto;margin-right:auto}}
.blog-hero .breadcrumb{{font-size:.8rem;color:var(--text-mid);margin-bottom:1rem}}
.blog-hero .breadcrumb a{{color:var(--accent)}}
.blog-hero h1{{font-family:var(--font-heading);font-size:clamp(1.8rem,4vw,2.5rem);color:var(--ocean);line-height:1.25;margin-bottom:1rem}}
.blog-hero h1::after{{content:'';display:block;width:60px;height:3px;background:var(--warm);border-radius:3px;margin-top:12px}}
.blog-hero .meta{{font-size:.82rem;color:var(--text-mid)}}

.blog-content{{max-width:720px;margin:0 auto;padding:0 clamp(16px,5vw,80px) 40px}}
.blog-content p{{font-size:1rem;line-height:1.8;color:#333;margin-bottom:1.5rem}}
.blog-content p.intro{{font-size:1.05rem;color:var(--ocean);font-weight:500;border-left:3px solid var(--accent);padding-left:1rem}}
.blog-content h2{{font-family:var(--font-heading);font-size:1.4rem;color:var(--ocean);margin:2rem 0 1rem}}

.cta-box{{background:var(--accent-light);border-radius:12px;padding:24px 28px;border-left:4px solid var(--accent);margin:2rem 0}}
.cta-box p{{margin:0!important;color:var(--text)!important;font-weight:500}}
.cta-box a{{color:var(--accent);font-weight:700}}

.blog-nav{{max-width:720px;margin:0 auto;padding:0 clamp(16px,5vw,80px) 40px;display:flex;gap:1rem;flex-wrap:wrap}}
.blog-nav a{{display:inline-block;padding:10px 24px;background:var(--accent);color:#fff;border-radius:8px;font-size:.85rem;font-weight:600;letter-spacing:1px;text-transform:uppercase;transition:background .2s,transform .2s}}
.blog-nav a:hover{{background:var(--accent-hover);transform:translateY(-1px);color:#fff}}
.blog-nav a.secondary{{background:transparent;color:var(--accent);border:2px solid var(--accent)}}
.blog-nav a.secondary:hover{{background:var(--accent-light);color:var(--accent)}}

.site-footer{{position:relative;background:linear-gradient(170deg,#0E4D5A 0%,#1B6B6A 30%,#2A7B6B 60%,#0D3F4F 100%);color:rgba(255,255,255,.85);padding:60px clamp(16px,5vw,80px) 0}}
.footer-grid{{display:grid;grid-template-columns:repeat(4,1fr);gap:2rem;max-width:1100px;margin:0 auto}}
.footer-col h3{{font-family:var(--font-heading);font-size:1rem;color:#fff;margin-bottom:1rem}}
.footer-col p,.footer-col a{{color:rgba(255,255,255,.7);font-size:.85rem;line-height:1.7;text-decoration:none;display:block}}
.footer-col a:hover{{color:var(--seafoam)}}
.footer-brand-name{{font-family:var(--font-heading);font-size:1.3rem;color:#fff;margin-bottom:.5rem}}
.footer-bottom{{border-top:1px solid rgba(255,255,255,.12);text-align:center;padding:1rem;font-size:.75rem;color:rgba(255,255,255,.5);margin-top:40px;max-width:1100px;margin-left:auto;margin-right:auto}}

@media(max-width:767px){{
  .nav-links,.nav-book{{display:none}}
  .footer-grid{{grid-template-columns:1fr 1fr}}
  .blog-hero h1{{font-size:1.6rem}}
}}
@media(max-width:480px){{
  .footer-grid{{grid-template-columns:1fr}}
}}
</style>
</head>
<body>

<div class="top-bar" id="top-bar">
  <a href="tel:+15419921887"><svg viewBox="0 0 24 24"><path d="M22 16.92v3a2 2 0 01-2.18 2 19.79 19.79 0 01-8.63-3.07 19.5 19.5 0 01-6-6 19.79 19.79 0 01-3.07-8.67A2 2 0 014.11 2h3a2 2 0 012 1.72c.127.96.361 1.903.7 2.81a2 2 0 01-.45 2.11L8.09 9.91a16 16 0 006 6l1.27-1.27a2 2 0 012.11-.45c.907.339 1.85.573 2.81.7A2 2 0 0122 16.92z"/></svg>(541) 992-1887</a>
  <div class="tb-divider"></div>
  <a href="{SITE['book']}" target="_blank"><svg viewBox="0 0 24 24"><path d="M4 4h16v16H4z" stroke-linejoin="round"/><path d="M4 10h16M10 4v16"/></svg>Book Online</a>
</div>

<nav class="nav" id="nav">
  <a href="../index.html" class="nav-logo"><img class="nav-logo-img" src="{SITE['logo']}" alt="The Nail Ladie"></a>
  <ul class="nav-links">
    <li><a href="../services.html">Services</a></li>
    <li><a href="../gallery.html">Gallery</a></li>
    <li><a href="../reviews.html">Reviews</a></li>
    <li><a href="../faq.html">FAQ</a></li>
    <li><a href="../visit.html">Visit</a></li>
  </ul>
  <a href="{SITE['book']}" target="_blank" class="nav-book">Book Now</a>
</nav>

<article>
<header class="blog-hero">
  <p class="breadcrumb"><a href="../index.html">Home</a> &rsaquo; <a href="index.html">Blog</a> &rsaquo; {title}</p>
  <h1>{title}</h1>
  <p class="meta">By Heather at The Nail Ladie &middot; Depoe Bay, Oregon</p>
</header>

<div class="blog-content">
{body_html}
</div>

<div class="blog-nav">
  <a href="{SITE['book']}" target="_blank">Book Your Appointment</a>
  <a href="../services.html" class="secondary">View Services &amp; Pricing</a>
</div>
</article>

<footer class="site-footer">
  <div class="footer-grid">
    <div class="footer-col">
      <div class="footer-brand-name">The Nail Ladie</div>
      <p>Premium nail care on the Oregon Coast.</p>
    </div>
    <div class="footer-col">
      <h3>Explore</h3>
      <a href="../services.html">Services</a>
      <a href="../gallery.html">Gallery</a>
      <a href="../reviews.html">Reviews</a>
    </div>
    <div class="footer-col">
      <h3>Visit</h3>
      <p>{SITE['addr']}</p>
      <a href="tel:+15419921887">{SITE['phone']}</a>
    </div>
    <div class="footer-col">
      <h3>Book</h3>
      <a href="{SITE['book']}" target="_blank">Book Online</a>
      <a href="tel:+15419921887">Call to Book</a>
    </div>
  </div>
  <div class="footer-bottom">&copy; 2026 The Nail Ladie. All rights reserved. Depoe Bay, Oregon.</div>
</footer>

<script>
const nav=document.getElementById('nav'),topBar=document.getElementById('top-bar');
window.addEventListener('scroll',()=>{{const s=window.scrollY>80;nav.classList.toggle('scrolled',s);if(topBar)topBar.classList.toggle('hidden',s)}},{{passive:true}});
</script>
</body>
</html>'''


def index_html(topics):
    items = ""
    for title, slug, desc, kw, cat, _ in topics:
        items += f'      <li><a href="{slug}.html">{title}</a><span class="blog-cat">{cat}</span></li>\n'

    return f'''<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>Blog | The Nail Ladie — Depoe Bay, Oregon Nail Salon</title>
<meta name="description" content="Nail care tips, trends, and Oregon Coast beauty guides from The Nail Ladie in Depoe Bay. Gel nails, lash extensions, nail art, stamping, and more.">
<link rel="canonical" href="{SITE['base']}/blog/">
<style>
*,*::before,*::after{{box-sizing:border-box;margin:0;padding:0}}
:root{{--bg:#FAF9F6;--accent:#1B6B6A;--accent-hover:#248F8D;--accent-light:#D4EEEE;--warm:#C4A06E;--seafoam:#5EC4C4;--ocean:#2A4F6B;--text:#1A1A1A;--text-mid:#555;--font-heading:Georgia,'Palatino Linotype','Book Antiqua',Palatino,'Times New Roman',serif;--sans:-apple-system,BlinkMacSystemFont,'Segoe UI',Roboto,'Helvetica Neue',Arial,sans-serif;--border:#B8D4DA;--ease:cubic-bezier(.25,.46,.45,.94)}}
html{{scroll-behavior:smooth}}body{{font-family:var(--sans);color:var(--text);background:var(--bg);line-height:1.6;-webkit-font-smoothing:antialiased}}
a{{color:var(--accent);text-decoration:none}}a:hover{{color:var(--accent-hover)}}

.top-bar{{position:fixed;top:0;left:0;right:0;z-index:102;background:var(--accent);color:#fff;display:flex;align-items:center;justify-content:center;gap:clamp(1rem,3vw,2.5rem);padding:6px clamp(1rem,3vw,2rem);font-size:.68rem;letter-spacing:1.5px;text-transform:uppercase}}
.top-bar a{{color:#fff;display:flex;align-items:center;gap:6px;transition:color .3s}}.top-bar a:hover{{color:var(--seafoam)}}
.top-bar svg{{width:14px;height:14px;stroke:currentColor;fill:none;stroke-width:1.5}}
.top-bar .tb-divider{{width:1px;height:12px;background:rgba(255,255,255,.25)}}

.nav{{position:fixed;top:30px;left:0;right:0;z-index:100;padding:0 clamp(1.5rem,4vw,3rem);height:80px;display:flex;align-items:center;justify-content:space-between;transition:all .5s var(--ease);background:rgba(255,255,255,.92);backdrop-filter:blur(20px);box-shadow:0 2px 20px rgba(0,0,0,.08)}}
.nav.scrolled{{top:0;background:rgba(250,250,248,.95);height:64px;box-shadow:0 1px 0 var(--border)}}
.top-bar.hidden{{transform:translateY(-100%);transition:transform .3s var(--ease)}}
.nav-logo{{display:flex;align-items:center;z-index:101}}.nav-logo-img{{height:80px;width:auto;transition:all .5s}}
.nav.scrolled .nav-logo-img{{height:50px}}
.nav-links{{display:flex;align-items:center;gap:2.5rem;list-style:none}}
.nav-links a{{font-size:.75rem;letter-spacing:1.5px;text-transform:uppercase;color:var(--text-mid);transition:color .3s;position:relative;text-decoration:none}}
.nav-links a::after{{content:'';position:absolute;bottom:-4px;left:0;width:0;height:1px;background:currentColor;transition:width .3s var(--ease)}}
.nav-links a:hover::after{{width:100%}}
.nav-book{{font-size:.7rem;letter-spacing:2px;text-transform:uppercase;padding:11px 26px;border:1px solid var(--accent);color:var(--accent);transition:all .3s var(--ease);text-decoration:none}}
.nav-book:hover{{background:var(--accent);color:#fff}}

.blog-header{{margin-top:110px;padding:60px clamp(16px,5vw,80px) 30px;max-width:900px;margin-left:auto;margin-right:auto;text-align:center}}
.blog-header h1{{font-family:var(--font-heading);font-size:clamp(2rem,5vw,3rem);color:var(--ocean)}}
.blog-header h1::after{{content:'';display:block;width:60px;height:3px;background:var(--warm);border-radius:3px;margin:12px auto 0}}
.blog-header p{{color:var(--text-mid);font-size:1.05rem;margin-top:1rem;max-width:600px;margin-left:auto;margin-right:auto}}

.blog-filter{{max-width:900px;margin:0 auto;padding:0 clamp(16px,5vw,80px) 20px;display:flex;flex-wrap:wrap;gap:8px;justify-content:center}}
.blog-filter button{{padding:6px 16px;border:1px solid var(--border);border-radius:20px;background:#fff;color:var(--text-mid);font-size:.78rem;cursor:pointer;transition:all .2s}}
.blog-filter button:hover,.blog-filter button.active{{background:var(--accent);color:#fff;border-color:var(--accent)}}

.blog-list{{max-width:900px;margin:0 auto;padding:10px clamp(16px,5vw,80px) 60px;list-style:none}}
.blog-list li{{border-bottom:1px solid #eee;padding:14px 0;display:flex;align-items:baseline;justify-content:space-between;gap:1rem}}
.blog-list li a{{font-size:1rem;color:var(--text);font-weight:500;transition:color .2s;flex:1}}
.blog-list li a:hover{{color:var(--accent)}}
.blog-cat{{font-size:.7rem;letter-spacing:1px;text-transform:uppercase;color:var(--text-mid);white-space:nowrap;background:var(--accent-light);padding:3px 10px;border-radius:12px}}

.site-footer{{position:relative;background:linear-gradient(170deg,#0E4D5A 0%,#1B6B6A 30%,#2A7B6B 60%,#0D3F4F 100%);color:rgba(255,255,255,.85);padding:60px clamp(16px,5vw,80px) 0}}
.footer-grid{{display:grid;grid-template-columns:repeat(4,1fr);gap:2rem;max-width:1100px;margin:0 auto}}
.footer-col h3{{font-family:var(--font-heading);font-size:1rem;color:#fff;margin-bottom:1rem}}
.footer-col p,.footer-col a{{color:rgba(255,255,255,.7);font-size:.85rem;line-height:1.7;text-decoration:none;display:block}}
.footer-col a:hover{{color:var(--seafoam)}}
.footer-brand-name{{font-family:var(--font-heading);font-size:1.3rem;color:#fff;margin-bottom:.5rem}}
.footer-bottom{{border-top:1px solid rgba(255,255,255,.12);text-align:center;padding:1rem;font-size:.75rem;color:rgba(255,255,255,.5);margin-top:40px;max-width:1100px;margin-left:auto;margin-right:auto}}
@media(max-width:767px){{
  .nav-links,.nav-book{{display:none}}
  .footer-grid{{grid-template-columns:1fr 1fr}}
  .blog-list li{{flex-direction:column;gap:.3rem}}
}}
@media(max-width:480px){{.footer-grid{{grid-template-columns:1fr}}}}
</style>
</head>
<body>

<div class="top-bar" id="top-bar">
  <a href="tel:+15419921887"><svg viewBox="0 0 24 24"><path d="M22 16.92v3a2 2 0 01-2.18 2 19.79 19.79 0 01-8.63-3.07 19.5 19.5 0 01-6-6 19.79 19.79 0 01-3.07-8.67A2 2 0 014.11 2h3a2 2 0 012 1.72c.127.96.361 1.903.7 2.81a2 2 0 01-.45 2.11L8.09 9.91a16 16 0 006 6l1.27-1.27a2 2 0 012.11-.45c.907.339 1.85.573 2.81.7A2 2 0 0122 16.92z"/></svg>(541) 992-1887</a>
  <div class="tb-divider"></div>
  <a href="{SITE['book']}" target="_blank"><svg viewBox="0 0 24 24"><path d="M4 4h16v16H4z" stroke-linejoin="round"/><path d="M4 10h16M10 4v16"/></svg>Book Online</a>
</div>

<nav class="nav" id="nav">
  <a href="../index.html" class="nav-logo"><img class="nav-logo-img" src="{SITE['logo']}" alt="The Nail Ladie"></a>
  <ul class="nav-links">
    <li><a href="../services.html">Services</a></li>
    <li><a href="../gallery.html">Gallery</a></li>
    <li><a href="../reviews.html">Reviews</a></li>
    <li><a href="../faq.html">FAQ</a></li>
    <li><a href="../visit.html">Visit</a></li>
  </ul>
  <a href="{SITE['book']}" target="_blank" class="nav-book">Book Now</a>
</nav>

<header class="blog-header">
  <h1>The Nail Ladie Blog</h1>
  <p>Nail care tips, trends, and Oregon Coast beauty guides from Depoe Bay's premier private salon.</p>
</header>

<div class="blog-filter">
  <button class="active" onclick="filterBlog('all')">All</button>
  <button onclick="filterBlog('nails')">Nails</button>
  <button onclick="filterBlog('lashes')">Lashes</button>
  <button onclick="filterBlog('pedicures')">Pedicures</button>
  <button onclick="filterBlog('location')">Local</button>
  <button onclick="filterBlog('seasonal')">Seasonal</button>
  <button onclick="filterBlog('educational')">Guides</button>
  <button onclick="filterBlog('trends')">Trends</button>
  <button onclick="filterBlog('tourism')">Tourism</button>
  <button onclick="filterBlog('lifestyle')">Lifestyle</button>
</div>

<ul class="blog-list" id="blog-list">
{items}
</ul>

<footer class="site-footer">
  <div class="footer-grid">
    <div class="footer-col"><div class="footer-brand-name">The Nail Ladie</div><p>Premium nail care on the Oregon Coast.</p></div>
    <div class="footer-col"><h3>Explore</h3><a href="../services.html">Services</a><a href="../gallery.html">Gallery</a><a href="../reviews.html">Reviews</a></div>
    <div class="footer-col"><h3>Visit</h3><p>{SITE['addr']}</p><a href="tel:+15419921887">{SITE['phone']}</a></div>
    <div class="footer-col"><h3>Book</h3><a href="{SITE['book']}" target="_blank">Book Online</a><a href="tel:+15419921887">Call to Book</a></div>
  </div>
  <div class="footer-bottom">&copy; 2026 The Nail Ladie. All rights reserved. Depoe Bay, Oregon.</div>
</footer>

<script>
const nav=document.getElementById('nav'),topBar=document.getElementById('top-bar');
window.addEventListener('scroll',()=>{{const s=window.scrollY>80;nav.classList.toggle('scrolled',s);if(topBar)topBar.classList.toggle('hidden',s)}},{{passive:true}});
function filterBlog(cat){{
  document.querySelectorAll('.blog-filter button').forEach(b=>b.classList.remove('active'));
  event.target.classList.add('active');
  document.querySelectorAll('#blog-list li').forEach(li=>{{
    const c=li.querySelector('.blog-cat').textContent.toLowerCase();
    li.style.display=(cat==='all'||c===cat)?'':'none';
  }});
}}
</script>
</body>
</html>'''


# ─── GENERATE ──────────────────────────────────────────────────────────────────
print(f"Generating {len(TOPICS)} blog posts...")

for i, (title, slug, desc, keyword, category, paragraphs) in enumerate(TOPICS, 1):
    html = blog_html(title, slug, desc, paragraphs, keyword, category)
    path = os.path.join(OUT, f"{slug}.html")
    with open(path, "w", encoding="utf-8") as f:
        f.write(html)
    print(f"  [{i:3d}/{len(TOPICS)}] {slug}.html")

# Generate index
idx = index_html(TOPICS)
with open(os.path.join(OUT, "index.html"), "w", encoding="utf-8") as f:
    f.write(idx)
print(f"\n  blog/index.html (listing page)")

print(f"\nDone! Generated {len(TOPICS)} blog posts + index in {OUT}")
