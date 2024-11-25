import requests

url = 'http://localhost:9696/predict'

sample = {'0_pre-RR': 206.0,
  '0_post-RR': 243.0,
  '0_pPeak': 0.047969956,
  '0_tPeak': 1.541606797,
  '0_rPeak': 1.509806577,
  '0_sPeak': 1.509806577,
  '0_qPeak': 0.011090966,
  '0_qrs_interval': 9,
  '0_pq_interval': 3,
  '0_qt_interval': 13,
  '0_st_interval': 1,
  '0_qrs_morph0': 0.011090966,
  '0_qrs_morph1': 0.013109427,
  '0_qrs_morph2': 0.167740782,
  '0_qrs_morph3': 0.583400545,
  '0_qrs_morph4': 1.119587456,
  '1_pre-RR': 206.0,
  '1_post-RR': 243.0,
  '1_pPeak': -0.034179402,
  '1_tPeak': 0.296782222,
  '1_rPeak': 0.064287214,
  '1_sPeak': -0.57742044,
  '1_qPeak': -0.038414812,
  '1_qrs_interval': 34,
  '1_pq_interval': 8,
  '1_qt_interval': 49,
  '1_st_interval': 7,
  '1_qrs_morph0': -0.038414812,
  '1_qrs_morph1': -0.033358336,
  '1_qrs_morph2': -0.028278429,
  '1_qrs_morph3': -0.024205756,
  '1_qrs_morph4': 0.05058648}

response = requests.post(url, json=sample).json()

print(response)


