# Draft · OSD-116 comment to Felix — S-05 Spec questions

**Status**: **SENT** as OSD-116 comment `c50250` on 2026-09-21 06:26 WIB, read back and
confirmed (total 153; all three mentions rendered as real mentions). Text as sent is
identical to the body below.

History: three send attempts on the evening of 2026-09-20 all timed out while the
Atlassian connector was degraded (repeated 60s timeouts on read and write, one
`502 Bad gateway`, one `You don't have permission to connect from this IP address`, and
`The app is not installed on this instance` on the Backend Operations connector). The
card was checked after each attempt and again before sending on 21 Sep — nothing had
landed, so there was no duplicate.

**Send to**: Jira issue `OSD-116`, as a new comment (not a reply).
**Account**: the repo owner's personal Atlassian connector. The Backend Operations
account cannot see project OSD.
**Format**: HTML, with real mentions.

| Mention | accountId |
| --- | --- |
| @Felix_HR | `712020:e5c38f7f-4fa8-4c37-a08e-029af3a09a87` |
| @Kent | `62cfa6e1bb346bdf82fac8f6` |
| @Alden | `5b666de62c9bd83c037070ae` |

**Why OSD-116 and not the 建造单 page**: 07.06 §三 归口表 row 1 — questions about a Spec's
business content (判断、字段、文案) go to the flow Owner on **该 Feature 的 Comment，@Owner**,
with a 1-working-day window (C-10). The 建造单 Comment is where §三 (e) puts the 开工对齐清单,
which is a separate artefact and was already filed on 19 Sep.

**Open choice not yet made**: item 3 (bot into the seven Collab channels) sits here per
Kent's routing (c50234 #5). Read literally, 07.06 §三 归口表 row 4 puts 频道 issues with
Alden via the 建造单 Comment. Left with Felix because only the channel owner can act.

---

## Body

【Spec questions → @Felix_HR】 Four items for you.

**1. Two Request Type names** (per @Kent c50227 #5). 04.7 registers both of this flow's
entries, but neither carries its name: RT-HR-DISCIPLINARY-SUBMIT reads
「双语Request Type／Slack展示名称待流程Owner确认」, RT-HR-DISCIPLINARY-EVENT has none. The
name forms the first segment of the master-ticket title (04.2 §五), and for the SUBMIT
entry it is also the Slack display name, as 04.7 itself notes. Format per 04.1 §四 →
04.0 §五: Chinese first · half-width middle dot with one space on each side · English
after. The name must not contain the full-width「｜」— that character splits titles, and
names containing it have broken automation twice before (NSE-1143 c49117／c49123). Until
both names exist neither Request Type can be built, and neither 04.7 row can be switched
to live under 04.7 §四「名称一致」.

**2. Three points the Spec requires but does not place** (routed to you by @Kent c50238,
who judged all three 业务歧义 rather than standard gaps).

**(a) How much of HR's reasoning is kept?** The Spec has HR record its basis at four
points — N07 (choosing the formal tool), N10 (upheld／not upheld), N14 (upheld／not
upheld), N17 (the consequence of a Failed PIP) — mandatory on whichever branch applies.
Should each keep its own separate record, or should there be one running record each
decision adds to? The difference is whether a later reader sees four distinct judgments
or one continuous history.

**(b) D-9 promises an explanation that nothing collects.** The N17 notice tells the
employee「结果说明：【Result Summary】」. The Spec collects the outcome as one of three
values — Completed／Extension／Failed — but nothing collects the sentence explaining it.
The nearest existing item is HR's basis at N17, which the Spec scopes to the Failed
consequence, while the notice promises a summary for all three outcomes. Who writes that
explanation, and at which step?

**(c) The duplicate mark has no place to live.** N05 marks a suspected duplicate and
carries the original case link along; N07 then requires HR to confirm whether it is the
same ongoing event before the case is linked or cancelled. The term appears in ⓪ 区, N05,
N07 and the technical-confirmation list, with no matching item in 增补区 A. It can be
recorded as an audit note that machines read, but the person reviewing at N07 needs to
see it before deciding. Should it be visible on the case itself?

**3. Bot into the seven department Collab channels — go-live blocker** (per @Kent c50234
#5). My 19 Sep 建造单 comment reported that `@sscos-bot` is in none of them; that comment
listed no action for you, so this is the explicit request: only the channel owner can
invite the bot. Two consequences: 04.11 §三 requires the bot to already be in a channel
before that channel can be registered, and 04.5 §七 item 22 makes an unregistered channel
a hard audit failure should the Spec re-enter structural audit. 04.11 (v2) currently
carries four rows — HR, Finance, BO and one retired key — and none of the seven.

**4. Two of the seven may be obsolete.** `collab-hr-inz9` and `collab-hr-marketing`
remain on your c49247 list, but both departments were merged into CRM (Alden, 2026-09-08;
both boards archived). Do those channels still serve those teams, or should their notices
go to `collab-hr-crm`?

The NTP position list standardisation, which N07／N14 recusal depends on, remains with
you and @Alden per @Kent c50227 #3.

—— Bambang

---

## Verification

Every claim was checked against the live source on 2026-09-20. Versions as read:

| Claim | Source | Result |
| --- | --- | --- |
| Both RT rows exist; SUBMIT reads「…待流程Owner确认」; EVENT has no name | 04.7, the two S-05 rows | verbatim |
| Neither entry is on the Portal | 04.7, Portal Group =「—（非 Portal 入口）」 | confirmed |
| Request type is the first segment of the **master-ticket** title only | 04.2 §五（子单 uses {执行动作}；「请求类型只在主单标题出现一次」） | confirmed |
| Bilingual short-string format | 04.1 **v46** §四 → 04.0 **v26** §五 | confirmed |
| Full-width「｜」ban + NSE-1143 c49117／c49123 | 04.0 **v26** §五 | verbatim |
| 04.7 §四「名称一致」 | 04.7 §四 | confirmed |
| `HR判定依据` four collection points incl. N17（Failed后果判定）; 必填「是（对应分支必填）」 | Spec **v62** table A | verbatim |
| D-9 belongs to N17 and prints「结果说明：【Result Summary】」 | Spec **v62** table D | verbatim |
| `PIP Result` = Completed／Extension／Failed; no field carries the narrative | Spec **v62** table A (34 rows) | confirmed |
| `疑似重复` in ⓪区, N05, N07, T-3; absent from table A | Spec **v62** | confirmed |
| Bot in none of the seven; that comment listed「无待确认项」 | 建造单 footer comment `2101870628`, 19 Sep | verbatim |
| Only the channel owner can invite the bot | Kent c50234 #5 | confirmed |
| Bot must be in the channel before it can be registered | 04.11 **v2** §三 | verbatim |
| 04.11 carries four rows, none of the seven | 04.11 **v2** §二 | confirmed |
| Unregistered channel = hard audit failure | 04.5 **v79** §七 item 22 | confirmed |
| Inz9／Marketing merged into CRM, boards archived | 04.1 **v46** CRM row | confirmed |
| NTP position list still with Felix and Alden | Kent c50227 #3 | confirmed |

Three errors found and fixed during the final pass: the opening attributed all four items
to c50238 (only items 2a–2c came from there); "first segment of every case title" was
wrong (sub-ticket titles do not carry the request type); and the paraphrase of 04.7 §四
said "platform display name" where the rule says「Portal 实际显示名」— the paraphrase was
dropped rather than reworded, since neither entry is a Portal entry.
