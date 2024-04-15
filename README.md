Written as part of the analysis project SHOWDOWN - A Comprehensive Analysis of Antivirus Software Effectiveness and Cost-Efficacy Against Modern Malware Threats.

Though this is an extremely simplified version of a real c2, it has the essential functionality that makes it dangerous and should necessitate AV to label it as malware: 

1. arbitrary remote command execution
2. data exfiltration
3. continuous communication

Some functionality this basic c2 is missing that real-world adversaries would have include: Multi-Channel Communication, Encryption and Obfuscation, Modularity and Extensibility, Stealth and Evasion Techniques, Persistance, Automated Tasking, and Access Control and Authentication. 

An abstract of the SHOWDOWN report below:

This report presents the findings of a comprehensive analysis aimed to evaluate the efficacy of Anti-Virus (AV) software in detecting three distinct malware payloads: Mimikatz, Meterpreter, and a custom Command and Control (C2) implant. Leveraging VirusTotal as the testing platform, we systematically assessed the detection rates of 60 leading AV solutions against variants of these malware, both in their original forms and when employing various obfuscation techniques. 

Our final results suggest that some AV are not prepared for custom malware attacks and heavily rely on static signature-based detection methods rather than dynamic behaviour analysis, underscoring the recommendation for AV software to evolve with more advanced detection strategies. An analysis against cost showed no direct correlation between AV cost and performance, indicating that both high and low detection rates are found in both free and paid AVs, and the more expensive AVs do not always provide the highest detection rates. Additionally, consumers are highly recommended to practise more caution with files regardless of AV presence.       

Project SHOWDOWN authors: Anni Wang (me), Connor Johst, Erik Dahl, and Jacob Newman
