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
- Bait post (profile only, max ONE per day, only for broad easy roles). Standard line (Levon's wording, 2026-10-25): "Want the link? Comment and send me a message with your field: history, law, finance, journalism or tech. I'll reply with the apply link." Adapt the field list to the role (languages for a language role, "Field: ..." for domain roles, tools or specialties otherwise); keep the rest of the sentence unchanged. No "Connect with me". The bait post carries no link. Do NOT prepare first-comment text (Buffer free has no first comment; Levon replies to commenters himself). Instead end the package with one line per bait post: "Reply link (for commenters): <exact talentsforai.com job URL with utm_content=comment>". Take the URL from the verified job page, never build it from the title (a guessed slug was dead on 2026-10-14). The company page and Facebook versions of the same job carry the links directly.

## Images (1080x1080 cards, style: white, big black headline, flat flags with country/language names, purple pay line)
- Build with `python3 tools/make_card.py spec.json out.png` (run `npm i` inside tools/ first for flag SVGs; needs playwright + chromium). See the docstring for the spec format. Flat SVG flags only (never wavy emoji). 1-4 flags big, 5-8 smaller in a 4x2 grid, 9+ smaller.
- Save cards to `cards/YYYY-MM-DD/<slug>.png`, commit, push to main. Public URL for Buffer: `https://raw.githubusercontent.com/levingtn27/tfai-cards/main/cards/YYYY-MM-DD/<slug>.png` (check it returns HTTP 200 before using). LOOK at each rendered card before using it (text fit, flags, pay correct).
- Push first: `git fetch origin main` then rebase/pull before pushing.

## Daily package (Levon's 8am Yerevan, weekdays)
1. 3 job posts x 3 channels (as above) + Telegram versions + image for each.
2. Comment list: 5-8 recent LinkedIn posts worth commenting on, each with a ready comment (specific, adds value, no spam). If real posts cannot be found, say so and ask Levon for targets. Never invent posts.
3. Analytics brief from the private repo `levingtn27/tfai-analytics`, file `analytics-latest.md` (GA4 property 515464087 + Search Console, pulled every morning at 07:30 by a launchd job on Levon's Mac mini and pushed there; see "Analytics feed" below). Call add_repo (owner levingtn27, repo tfai-analytics, access read), `git clone --depth 1`, read the file. Check its "Pulled:" date: if older than 1 day say "analytics stale (last pull <date>)" and use it only as background; if the repo or file is unavailable write "analytics unavailable today"; never estimate numbers. Do NOT use Windsor for GA4/Search Console (free plan returns only an empty row since 2026-10-22). Use the file's tables for: Yesterday and 7 days, top pages, channels, Search Console movers, 2-3 concrete suggestions (SEO, tools/affiliate pages, email, new sources, revenue). Mondays: weekly summary + one article idea ('is X legit' style). Known: /blog/is-mercor-legit is the best page (647 clicks/28d, position 6.2); Appen/DataAnnotation/Outlier legit pages have impressions but low CTR.
4. Wed and Fri: one personal LinkedIn post for Levon's profile. Ask him 2-3 short questions about what really happened that week (numbers, results, lessons) and for photos. Never invent stories or numbers. His best posts were personal stories with numbers.
5. Save the 9 job posts as Buffer DRAFTS (saveToDraft true) with images, so nothing publishes by accident. After Levon says approve (or sends edits), schedule them (edit_post with mode customScheduled and dueAt; keep assets and metadata).
6. Final message: the package, clearly, ending with a request to reply "approve" or edits.

## Known facts
- Analytics feed (since 2026-10-26): Levon's Mac mini runs ~/Documents/tfai-status-app/analytics-pull/daily.sh at 07:30 (launchd com.tfai.analytics), which pulls GA4 + Search Console with a service account, writes analytics-latest.md and pushes it to the private repo levingtn27/tfai-analytics. Only that summary leaves the Mac; the key stays local. Biggest known SEO opportunity (2026-10-26): /blog/is-appen-legit-an-honest-2026-review has ~54k impressions, 15 clicks, position 9.2 (query "appen review"); rewrite its title/meta. The site job pages come from SME API, Micro1, Turing feeds.
- Job schema warnings in Search Console (validThrough, baseSalary.value) are non-critical; decided to leave them.

## UTM links (added 2026-10-10)
Every talentsforai.com link in a post gets: ?utm_source=<linkedin|facebook|telegram>&utm_medium=social&utm_campaign=jobs&utm_content=<profile|page>
(profile = Levon's LinkedIn profile, page = company page / Facebook). Bait posts carry no link in the post; the reply link Levon sends to commenters uses utm_content=comment.

## Learnings from the 2026-10-10 test
- A Buffer post stays status "draft" if edit_post is given customScheduled without saveToDraft:false; pass saveToDraft:false plus text and assets to make it "scheduled".
- Use list_posts with small first=N and status/channel filters; unfiltered output is ~100k chars.
- Skip any job page whose body does not match its title or shows "[Rate/Salary]" style placeholders (known broken Turing pages: mathematics-expert-111563, computer-science-stem-111548, domain-expert-python-111872, life-sciences-subject-matter-expert-biology-111854).
- Scheduled posts count toward the 10-per-channel free-plan queue limit.

## Turing roles: verify before posting (added 2026-10-12)
The Turing job feed sometimes carries a description that does not match the job title (Turing's own data; the scraper copies it faithfully). Known examples: ~20 jobs with dermatology text under unrelated titles, and 111563 with hardware text and "[Rate/Salary]" placeholders.
- Before posting a Turing role, check that the page's one-liner and body fit the title, contain no "[...]" placeholders, and are not the dermatology / "clinical reviews" text unless the title is medical.
- If unsure, pick an SME Careers or Micro1 role instead. Mention in the package which Turing roles were skipped and why.
- Verified OK so far: Business Consulting experts (111319), Finance experts (111315, feed text consistent).

## Eligibility wording (added 2026-10-14, Levon's standing rule)
Never write "No countries are listed", "check eligibility when you apply", "hours/duration aren't listed", "terms vary by region" or any similar not-listed / check-your-region disclaimer in posts or Telegram texts. Only state restrictions the page actually imposes (e.g. "Outside the US", "US only", PST overlap). If a page gives no countries, simply say nothing about it.

## Telegram follow line (added 2026-10-15, Levon's standing rule)
Every post on every channel (profile, company page, Facebook, and bait posts) ends, just before the hashtags, with: `📲 All links and new roles daily on Telegram: https://t.me/talentsforai` (no UTM on this link). Telegram's channel holds all the links.
