# Talents for AI daily social playbook

Owner: Levon Gevorgyan (founder, talentsforai.com). Everything is approved by Levon before it is scheduled. Never post, schedule or send without his explicit "approve".

## Channels (Buffer org 6a21b6a32d4d87722f01c048, free plan: max 10 scheduled posts PER CHANNEL, no first comment, images need a public URL)
- LinkedIn personal profile `levon-tfa`: 6a21b853c687a22dd45ea723  (3 job posts/day, ONE is a comment-bait post)
- LinkedIn company page `talents-for-ai`: 6a21b853c687a22dd45ea724  (same 3 jobs, links in text, NO bait, no "tag someone" line)
- Facebook page `Talents for AI`: 6ac9d50f6a5c39ccb66db01e  (same 3 jobs, links in text, NO bait; create_post needs metadata {"facebook":{"type":"post"}})
- Telegram: no tool. Prepare a Telegram text per post for Levon to paste himself (direct talentsforai.com links, flags, short).
- Times (Asia/Yerevan, +04:00): 11:00, 13:30, 17:00, the same on all channels. Weekdays only. Schedule only after approval.

## Job selection
- Sources: SME Careers, Micro1, Turing. NEVER Mercor (Mercor does not accept referrals from Armenia, Levon's country).
- Find roles on talentsforai.com (sitemaps https://talentsforai.com/job-sitemap.xml and job-sitemap2.xml; each job page shows pay, source, requirements). Verify pay, location and requirements on EVERY page you mention before writing. Pay can differ per page.
- Prefer broad, easy, high-reach roles (language experts, survey, generalist), visible pay, soft requirements, worldwide eligibility. Do not repeat a role posted in the last 7 days (check Buffer sent and scheduled posts).
- If the SME listing restricts countries but our page says "Worldwide", the page is wrong: front-load the real countries in the post and tell Levon about the page problem.
- If a role says there is no active project yet, say so honestly in the post.
- If a post covers several languages/roles: ONE link per language/role (never one link for several), and the card shows ALL flags.

## Post style
- No em dashes. Max 2 hashtags (#AIJobs #RemoteWork). Short punchy lines. Eligibility restrictions first.
- Header line like: `🌍 [HIRING] Role - up to $X/h`, then `Remote · Contract · Weekly pay` only if true, what you'd do, good fit checklist with ✅, branding line `SME Careers · via Talents for AI` or `Micro1 · via Talents for AI`, then the link(s), then (profile only) a "Tag someone ..." line.
- Flags in text: a flag emoji before each language/country. Levon approved the current flag choices (language is a language; flags are fine as is).
- Bait post (profile only, max ONE per day, only for broad easy roles): "Want the link? Connect with me and comment your language/role: X, Y or Z. I'll reply with the apply link." Give Levon the first-comment text with all links to paste (Buffer free cannot do first comments). The company page and Facebook versions of the same job carry the links directly.

## Images (1080x1080 cards, style: white, big black headline, flat flags with country/language names, purple pay line)
- Build with `python3 tools/make_card.py spec.json out.png` (run `npm i` inside tools/ first for flag SVGs; needs playwright + chromium). See the docstring for the spec format. Flat SVG flags only (never wavy emoji). 1-4 flags big, 5-8 smaller in a 4x2 grid, 9+ smaller.
- Save cards to `cards/YYYY-MM-DD/<slug>.png`, commit, push to main. Public URL for Buffer: `https://raw.githubusercontent.com/levingtn27/tfai-cards/main/cards/YYYY-MM-DD/<slug>.png` (check it returns HTTP 200 before using). LOOK at each rendered card before using it (text fit, flags, pay correct).
- Push first: `git fetch origin main` then rebase/pull before pushing.

## Daily package (Levon's 8am Yerevan, weekdays)
1. 3 job posts x 3 channels (as above) + Telegram versions + image for each.
2. Comment list: 5-8 recent LinkedIn posts worth commenting on, each with a ready comment (specific, adds value, no spam). If real posts cannot be found, say so and ask Levon for targets. Never invent posts.
3. Analytics brief with Windsor: GA4 account 515464087 (snake_case fields: sessions, totalusers, newusers, page_path, session_default_channel_group, event_count) and Search Console connector `searchconsole` (fields query, pagepath, clicks, impressions, position). Yesterday and 7 days, top pages, channels, Search Console movers, 2-3 concrete suggestions (SEO, tools/affiliate pages, email, new sources, revenue). Mondays: weekly summary + one article idea ('is X legit' style). Known: /blog/is-mercor-legit is the best page (647 clicks/28d, position 6.2); Appen/DataAnnotation/Outlier legit pages have impressions but low CTR.
4. Wed and Fri: one personal LinkedIn post for Levon's profile. Ask him 2-3 short questions about what really happened that week (numbers, results, lessons) and for photos. Never invent stories or numbers. His best posts were personal stories with numbers.
5. Save the 9 job posts as Buffer DRAFTS (saveToDraft true) with images, so nothing publishes by accident. After Levon says approve (or sends edits), schedule them (edit_post with mode customScheduled and dueAt; keep assets and metadata).
6. Final message: the package, clearly, ending with a request to reply "approve" or edits.

## Known facts
- Search Console and GA4 are connected in Windsor. The site job pages come from SME API, Micro1, Turing feeds.
- Job schema warnings in Search Console (validThrough, baseSalary.value) are non-critical; decided to leave them.
