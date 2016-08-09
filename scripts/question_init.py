# Include this line at the beginning of every script.
import environment

from pcari.models import QuantitativeQuestion, QualitativeQuestion

quantitative_q = [
"We live in an area that is safe from typhoons and floods.",
"The barangay has a system that warns the community about approaching typhoons or floods.",
"The barangay declogs sewers and dredges waterways prior to the typhoon and flooding season.",
"Our barangay is prepared to respond to the needs of the community (food, shelter, rescue) during typhoons and flooding.",
"We have sufficient knowledge of what to do in times of typhoons and floods.",
"We have enough supplies (food, equipment, emergency kit) at home in case there is a typhoon or flooding."
]

qualitative_q = [
"How can your local government unit help communities become better prepared for a typhoon or flood?"
]

for q in quantitative_q:
	new_q = QuantitativeQuestion(question=q)
	new_q.save()

for q in qualitative_q:
	new_q = QualitativeQuestion(question=q)
	new_q.save()