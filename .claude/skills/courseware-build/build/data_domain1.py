"""
Domain 1 — Get Started with Six Sigma Project.

Labs 1-4. Core assessed labs use the Contoso Service Desk scenario (the same
scenario as the Case Study assessment) so the courseware and assessment align.
Grounded in the CSSC "Six Sigma: A Complete Step-by-Step Guide" body of knowledge
and the original v20 trainer deck activities.
"""

DOMAIN1 = [
    dict(
        num=1, topic=0,
        title="Yellow Belt Role, Certification Paths, and Improvement Scenario",
        objective="Explain the Yellow Belt role and select a suitable improvement scenario (A1).",
        desc="Establish what a Lean Six Sigma Yellow Belt is accountable for, how the belt "
             "pathway progresses from White to Master Black Belt, and choose a small, "
             "manageable improvement scenario to carry through the whole course.",
        build="A Yellow Belt responsibility table and a selected improvement scenario.",
        services="Belt role matrix, CSSC certification pathway, project selection criteria",
        steps=[
            ("Define the Yellow Belt role — list at least four responsibilities and your contribution to each.", ""),
            ("Compare the White, Yellow, Green, Black and Master Black Belt pathways in a table.", ""),
            ("Review the Contoso Service Desk scenario: tickets are slow to be assigned and status is unclear.", ""),
            ("Test your scenario against the 'good project' criteria — day-to-day work, manageable, aligned to business goals, data available.", ""),
            ("Record why a Yellow Belt supports rather than leads this improvement.", ""),
        ],
        test="You can state the Yellow Belt role in one sentence and justify your scenario against all four selection criteria.",
    ),
    dict(
        num=2, topic=1,
        title="Lean, Six Sigma, Waste, Voice of Customer, and Value",
        objective="Apply Lean and Six Sigma concepts — value, waste, defects, variation (K1, A2).",
        desc="Separate what the customer actually values from the waste that surrounds it. "
             "Capture the Voice of the Customer, translate it into measurable CTQ requirements, "
             "and run a waste walk using the eight wastes (DOWNTIME).",
        build="A VOC-to-CTQ translation table, a value-added analysis, and a waste walk log.",
        services="VOC, CTQ tree, DOWNTIME eight wastes, value-added analysis",
        steps=[
            ("Capture the Voice of the Customer — record at least five verbatim customer statements.", ""),
            ("Translate each VOC statement into a need, then into a measurable CTQ requirement.", ""),
            ("Classify each process activity as value-added, business-value-added or non-value-added.", ""),
            ("Conduct a waste walk and tag each observation against the eight wastes (DOWNTIME).", ""),
            ("Distinguish a defect (output fails CTQ) from waste (effort the customer will not pay for).", ""),
            ("Identify which single waste type appears most often in your scenario.", ""),
        ],
        test="Every CTQ is measurable with a target, and each waste observation is tagged to one of the eight waste types.",
    ),
    dict(
        num=3, topic=1,
        title="SIPOC, Process Mapping, Handoffs, and SME Support",
        objective="Map a process with SIPOC and a detailed process map to expose handoffs (A2, A3).",
        desc="Build the macro 'as-is' view with SIPOC, then drill into a detailed process map "
             "that shows every actor, system and handoff — the points where delay and defects "
             "are actually created.",
        build="A completed SIPOC and a detailed process map with pain points marked.",
        services="SIPOC, process flowchart, swimlane map, standard process symbols",
        steps=[
            ("Set the process boundaries — agree the explicit start and stop points first.", ""),
            ("Build the SIPOC: Suppliers, Inputs, Process (5-7 high-level steps), Outputs, Customers.", ""),
            ("Expand into a detailed process map: Step, Actor, Activity, System, Handoff.", ""),
            ("Draw the same flow as a swimlane map so each actor's lane makes handoffs obvious.", ""),
            ("Mark pain points — delays, rework loops, unclear ownership and handoff risks.", ""),
            ("Prepare SME notes for the Green Belt: what you observed and what needs validation.", ""),
        ],
        test="Your SIPOC has all five columns populated and every handoff on the detailed map has a named owner on both sides.",
    ),
    dict(
        num=4, topic=1, elective=True,
        title="Elective — PDCA Small Improvement Project Charter",
        objective="Charter a small improvement using PDCA with a measurable goal (A1, A2).",
        desc="Not every improvement needs a full DMAIC project. Use PDCA to charter a small, "
             "fast improvement that a Yellow Belt can run under guidance — with a problem "
             "statement, a measurable goal and a defined check point.",
        build="A one-page PDCA charter with problem statement, goal, scope and success measure.",
        services="PDCA cycle, problem/goal statements, scope in-out, stakeholder list",
        steps=[
            ("Map the four PDCA phases to concrete actions for your scenario.", ""),
            ("Write the problem statement: process, time period, measurable issue and impact — no solution.", ""),
            ("Write a measurable goal statement: metric, baseline, target and date.", ""),
            ("Define scope with an explicit in-scope / out-of-scope table to prevent scope creep.", ""),
            ("Identify stakeholders and the decision you will make after the Check phase.", ""),
            ("Confirm the improvement is small enough to test within two weeks.", ""),
        ],
        test="Your goal statement contains a metric, a baseline, a target and a date, and your problem statement names no solution.",
    ),
]
