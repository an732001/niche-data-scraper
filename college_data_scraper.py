import bs4
import json
import unidecode
from progressbar import ProgressBar

from urllib.request import urlopen as uReq
from bs4 import BeautifulSoup as soup

# progressbar object
pbar = ProgressBar()

# write to json function
def writeToJSONFile(path, fileName, data):
    filePathNameWExt = './' + path + '/' + fileName + '.json'
    with open(filePathNameWExt, 'w') as fp:
        json.dump(data, fp)
# replace all those if statements with this clean function sOON
def objectExists(x):
	if (x != None):
		return x.span.text
	else:
		return ''

# path and name of file 
path = './'
fileName = 'college-data-18'
data = {}

urls = ['https://www.niche.com/colleges/university-of-ottawa/', 'https://www.niche.com/colleges/monash-university/', 'https://www.niche.com/colleges/university-of-calgary/', 'https://www.niche.com/colleges/university-of-british-columbia/', 'https://www.niche.com/colleges/concordia-university---montreal/', 'https://www.niche.com/colleges/mcmaster-university/', 'https://www.niche.com/colleges/mcgill-university/', 'https://www.niche.com/colleges/university-of-western-ontario/', 'https://www.niche.com/colleges/university-of-victoria/', 'https://www.niche.com/colleges/university-of-aberdeen/', 'https://www.niche.com/colleges/humber-college-institute-of-technology--and--advanced-learning/', 'https://www.niche.com/colleges/trinity-college-dublin/', 'https://www.niche.com/colleges/university-of-puerto-rico---mayaguez/', 'https://www.niche.com/colleges/university-of-puerto-rico---rio-piedras/', 'https://www.niche.com/colleges/universidad-del-turabo/', 'https://www.niche.com/colleges/bangor-university/', 'https://www.niche.com/colleges/universidad-metropolitana/', 'https://www.niche.com/colleges/middle-georgia-state-university/', 'https://www.niche.com/colleges/universidad-del-este/', 'https://www.niche.com/colleges/thompson-rivers-university/', 'https://www.niche.com/colleges/national-university-college---bayamon/', 'https://www.niche.com/colleges/university-of-north-georgia---gainesville/', 'https://www.niche.com/colleges/inter-american-university-of-puerto-rico/', 'https://www.niche.com/colleges/pontifical-catholic-university-of-puerto-rico---ponce/', 'https://www.niche.com/colleges/pensacola-christian-college/', 'https://www.niche.com/colleges/parsons-school-of-design---the-new-school/', 'https://www.niche.com/colleges/inter-american-university-of-puerto-rico---ponce/', 'https://www.niche.com/colleges/inter-american-university-of-puerto-rico---bayamon/', 'https://www.niche.com/colleges/university-of-puerto-rico---bayamon/', 'https://www.niche.com/colleges/london-school-of-economics--and--political-science/', 'https://www.niche.com/colleges/university-of-sacred-heart/', 'https://www.niche.com/colleges/inter-american-university-of-puerto-rico---san-german/', 'https://www.niche.com/colleges/university-of-puerto-rico---arecibo/', 'https://www.niche.com/colleges/regents-american-college-london/', 'https://www.niche.com/colleges/inter-american-university-of-puerto-rico---arecibo/', 'https://www.niche.com/colleges/inter-american-university-of-puerto-rico---aguadilla/', 'https://www.niche.com/colleges/university-of-puerto-rico---humacao/', 'https://www.niche.com/colleges/university-of-puerto-rico---cayey/', 'https://www.niche.com/colleges/university-of-puerto-rico---aguadilla/', 'https://www.niche.com/colleges/university-of-puerto-rico---carolina/', 'https://www.niche.com/colleges/chamberlain-college-of-nursing---addison/', 'https://www.niche.com/colleges/university-of-houston---clear-lake/', 'https://www.niche.com/colleges/university-of-puerto-rico---ponce/', 'https://www.niche.com/colleges/university-of-guam/', 'https://www.niche.com/colleges/university-of-the-people/', 'https://www.niche.com/colleges/university-of-north-texas-at-dallas/', 'https://www.niche.com/colleges/st-josephs-college---long-island/', 'https://www.niche.com/colleges/beth-medrash-govoha/', 'https://www.niche.com/colleges/st-thomas-university---canada/', 'https://www.niche.com/colleges/colorado-state-university---global-campus/', 'https://www.niche.com/colleges/governors-state-university/', 'https://www.niche.com/colleges/texas-a-and-m-university---galveston/', 'https://www.niche.com/colleges/university-of-phoenix---las-vegas/', 'https://www.niche.com/colleges/inter-american-university-of-puerto-rico---fajardo/', 'https://www.niche.com/colleges/polytechnic-university-of-puerto-rico/', 'https://www.niche.com/colleges/new-york-institute-of-technology---manhattan-campus/', 'https://www.niche.com/colleges/edic-college/', 'https://www.niche.com/colleges/inter-american-university-of-puerto-rico---barranquitas/', 'https://www.niche.com/colleges/inter-american-university-of-puerto-rico---guayama/', 'https://www.niche.com/colleges/eugene-lang-college-of-liberal-arts---the-new-school/', 'https://www.niche.com/colleges/university-of-phoenix---southern-arizona/', 'https://www.niche.com/colleges/capella-university/', 'https://www.niche.com/colleges/florida-polytechnic-university/', 'https://www.niche.com/colleges/texas-tech-university-health-sciences-center/', 'https://www.niche.com/colleges/university-of-the-virgin-islands/', 'https://www.niche.com/colleges/alberta-college-of-art--and--design/', 'https://www.niche.com/colleges/colegio-universitario-de-san-juan/', 'https://www.niche.com/colleges/athens-state-university/', 'https://www.niche.com/colleges/pontifical-catholic-university-of-puerto-rico---mayaguez/', 'https://www.niche.com/colleges/bayamon-central-university/', 'https://www.niche.com/colleges/atlantic-university-college/', 'https://www.niche.com/colleges/university-of-puerto-rico---utuado/', 'https://www.niche.com/colleges/miller-motte-college---wilmington/', 'https://www.niche.com/colleges/central-methodist-university---college-of-graduate--and--extended-studies/', 'https://www.niche.com/colleges/universidad-adventista-de-las-antillas/', 'https://www.niche.com/colleges/university-of-south-florida---sarasota-manatee/', 'https://www.niche.com/colleges/brandman-university/', 'https://www.niche.com/colleges/national-university-college---ponce/', 'https://www.niche.com/colleges/university-of-phoenix---north-florida/', 'https://www.niche.com/colleges/florida-institute-of-technology---online/', 'https://www.niche.com/colleges/edp-university-of-puerto-rico---san-juan/', 'https://www.niche.com/colleges/national-university-college---rio-grande/', 'https://www.niche.com/colleges/northern-marianas-college/', 'https://www.niche.com/colleges/national-university-college---arecibo/', 'https://www.niche.com/colleges/loma-linda-university/', 'https://www.niche.com/colleges/caribbean-university---bayamon/', 'https://www.niche.com/colleges/saint-louis-university---madrid/', 'https://www.niche.com/colleges/university-of-phoenix---san-antonio/', 'https://www.niche.com/colleges/university-of-phoenix---west-florida/', 'https://www.niche.com/colleges/john-cabot-university/', 'https://www.niche.com/colleges/university-of-phoenix---columbus-ga/', 'https://www.niche.com/colleges/azusa-pacific-university---online/', 'https://www.niche.com/colleges/the-american-university-of-paris/', 'https://www.niche.com/colleges/national-university-college---caguas/', 'https://www.niche.com/colleges/university-of-oklahoma-health-sciences-center/', 'https://www.niche.com/colleges/university-of-phoenix---augusta/', 'https://www.niche.com/colleges/university-of-maryland---baltimore/', 'https://www.niche.com/colleges/university-of-nebraska-medical-center/', 'https://www.niche.com/colleges/atenas-college/', 'https://www.niche.com/colleges/louisiana-state-university-health-sciences-center---new-orleans/', 'https://www.niche.com/colleges/edp-university-of-puerto-rico---san-sebastian/', 'https://www.niche.com/colleges/university-of-texas---health-science-center-at-san-antonio/', 'https://www.niche.com/colleges/thomas-jefferson-university/', 'https://www.niche.com/colleges/jacobs-university---bremen/', 'https://www.niche.com/colleges/texas-a-and-m-university---central-texas/', 'https://www.niche.com/colleges/university-of-texas---medical-branch-at-galveston/', 'https://www.niche.com/colleges/american-samoa-community-college/', 'https://www.niche.com/colleges/huertas-junior-college/', 'https://www.niche.com/colleges/columbia-central-university---caguas/', 'https://www.niche.com/colleges/university-of-memphis---lambuth/', 'https://www.niche.com/colleges/berkeley-college---woodbridge/', 'https://www.niche.com/colleges/university-of-texas---health-science-center-at-houston/', 'https://www.niche.com/colleges/barnes-jewish-college---goldfarb-school-of-nursing/', 'https://www.niche.com/colleges/samuel-merritt-university/', 'https://www.niche.com/colleges/american-university-of-puerto-rico---manati/', 'https://www.niche.com/colleges/the-college-at-southeastern/', 'https://www.niche.com/colleges/west-coast-university---dallas/', 'https://www.niche.com/colleges/platt-college---riverside/', 'https://www.niche.com/colleges/hult-international-business-school/', 'https://www.niche.com/colleges/roseman-university-of-health-sciences/', 'https://www.niche.com/colleges/resurrection-university/', 'https://www.niche.com/colleges/minerva-schools-at-keck-graduate-institute/', 'https://www.niche.com/colleges/pontifical-catholic-university-of-puerto-rico---arecibo/', 'https://www.niche.com/colleges/university-of-arkansas-for-medical-sciences/', 'https://www.niche.com/colleges/westcliff-university/', 'https://www.niche.com/colleges/caribbean-university---ponce/', 'https://www.niche.com/colleges/university-of-management--and--technology/', 'https://www.niche.com/colleges/new-england-school-of-communications/', 'https://www.niche.com/colleges/american-university-of-puerto-rico---bayamon/', 'https://www.niche.com/colleges/patten-university/', 'https://www.niche.com/colleges/cuny-graduate-school--and--university-center/', 'https://www.niche.com/colleges/san-diego-state-university---imperial-valley/', 'https://www.niche.com/colleges/baker-college-of-port-huron/', 'https://www.niche.com/colleges/springfield-college---school-of-professional-and-continuing-studies/', 'https://www.niche.com/colleges/centro-de-estudios-multidisciplinarios---san-juan/', 'https://www.niche.com/colleges/the-american-university-of-rome/', 'https://www.niche.com/colleges/flagler-college---tallahassee/', 'https://www.niche.com/colleges/saint-lukes-college-of-health-sciences/', 'https://www.niche.com/colleges/berkeley-college---white-plains/', 'https://www.niche.com/colleges/berkeley-college---newark/', 'https://www.niche.com/colleges/oregon-state-university---cascades/', 'https://www.niche.com/colleges/landmark-college/', 'https://www.niche.com/colleges/university-of-mississippi-medical-center/', 'https://www.niche.com/colleges/humacao-community-college/', 'https://www.niche.com/colleges/escuela-de-artes-plasticas-de-puerto-rico/', 'https://www.niche.com/colleges/flashpoint-chicago/', 'https://www.niche.com/colleges/beacon-college/', 'https://www.niche.com/colleges/cox-college/', 'https://www.niche.com/colleges/linfield-college---school-of-nursing/', 'https://www.niche.com/colleges/schiller-international-university/', 'https://www.niche.com/colleges/doane-university---lincoln-grand-island/', 'https://www.niche.com/colleges/university-of-puerto-rico---medical-sciences/', 'https://www.niche.com/colleges/centro-de-estudios-multidisciplinarios---humacao/', 'https://www.niche.com/colleges/saint-francis-medical-center-college-of-nursing---illinois/', 'https://www.niche.com/colleges/north-american-university/', 'https://www.niche.com/colleges/south-university---austin/', 'https://www.niche.com/colleges/berkeley-college---brooklyn/', 'https://www.niche.com/colleges/dewey-university---manati/', 'https://www.niche.com/colleges/touro-university---worldwide/', 'https://www.niche.com/colleges/medical-university-of-south-carolina/', 'https://www.niche.com/colleges/strayer-university---global-region/', 'https://www.niche.com/colleges/strayer-university---texas/', 'https://www.niche.com/colleges/puerto-rico-conservatory-of-music/', 'https://www.niche.com/colleges/charter-oak-state-college/', 'https://www.niche.com/colleges/parker-university/', 'https://www.niche.com/colleges/universal-technology-college-of-puerto-rico/', 'https://www.niche.com/colleges/allen-college/', 'https://www.niche.com/colleges/chamberlain-college-of-nursing---atlanta/', 'https://www.niche.com/colleges/university-of-texas---md-anderson-cancer-center/', 'https://www.niche.com/colleges/american-university-of-health-sciences/', 'https://www.niche.com/colleges/chamberlain-college-of-nursing---jacksonville/', 'https://www.niche.com/colleges/carlos-albizu-university---san-juan/', 'https://www.niche.com/colleges/gnomon-school-of-visual-effects/', 'https://www.niche.com/colleges/dewey-university---carolina/', 'https://www.niche.com/colleges/texas-a-and-m-health-science-center/', 'https://www.niche.com/colleges/dewey-university---hato-rey/', 'https://www.niche.com/colleges/caribbean-university---carolina/', 'https://www.niche.com/colleges/platt-college---aurora/', 'https://www.niche.com/colleges/blessing-rieman-college-of-nursing/', 'https://www.niche.com/colleges/southwestern-baptist-theological-seminary/', 'https://www.niche.com/colleges/sentara-college-of-health-sciences/', 'https://www.niche.com/colleges/fashion-institute-of-design--and--merchandising---san-francisco/', 'https://www.niche.com/colleges/the-school-of-jazz--and--contemporary-music---the-new-school/', 'https://www.niche.com/colleges/corcoran-school-of-art-and-design/', 'https://www.niche.com/colleges/bon-secours-memorial-college-of-nursing/', 'https://www.niche.com/colleges/oregon-health--and--science-university/', 'https://www.niche.com/colleges/mayo-school-of-health-sciences/', 'https://www.niche.com/colleges/ottawa-university---kansas-city/', 'https://www.niche.com/colleges/suny-downstate-medical-center/', 'https://www.niche.com/colleges/golden-gate-university/', 'https://www.niche.com/colleges/ottawa-university---phoenix/', 'https://www.niche.com/colleges/trine-university---regional/', 'https://www.niche.com/colleges/centro-de-estudios-multidisciplinarios---bayamon/', 'https://www.niche.com/colleges/the-kings-university---california/', 'https://www.niche.com/colleges/south-university---cleveland/', 'https://www.niche.com/colleges/studio-school/', 'https://www.niche.com/colleges/mgh-institute-of-health-professions/', 'https://www.niche.com/colleges/caribbean-university---vega-baja/', 'https://www.niche.com/colleges/universidad-teologica-del-caribe/', 'https://www.niche.com/colleges/south-university---novi/', 'https://www.niche.com/colleges/columbia-central-university---yauco/', 'https://www.niche.com/colleges/wellington-shaw-christian-university/', 'https://www.niche.com/colleges/south-florida-bible-college--and--theological-seminary/', 'https://www.niche.com/colleges/lakeview-college-of-nursing/', 'https://www.niche.com/colleges/goddard-college/', 'https://www.niche.com/colleges/northwestern-polytechnic-university/', 'https://www.niche.com/colleges/helene-fuld-college-of-nursing/', 'https://www.niche.com/colleges/suny-upstate-medical-university/', 'https://www.niche.com/colleges/bastyr-university/', 'https://www.niche.com/colleges/saint-anthony-college-of-nursing/', 'https://www.niche.com/colleges/chamberlain-college-of-nursing---houston/', 'https://www.niche.com/colleges/chamberlain-college-of-nursing---st-louis-westline/', 'https://www.niche.com/colleges/chamberlain-college-of-nursing---arlington/', 'https://www.niche.com/colleges/purdue-university-global---augusta-campus/', 'https://www.niche.com/colleges/university-of-the-west/', 'https://www.niche.com/colleges/amridge-university/', 'https://www.niche.com/colleges/marian-court-college/', 'https://www.niche.com/colleges/simmons-college---kentucky/', 'https://www.niche.com/colleges/rabbinical-college-of-long-island/', 'https://www.niche.com/colleges/mannes-school-of-music---the-new-school/', 'https://www.niche.com/colleges/saint-joseph-seminary-college/', 'https://www.niche.com/colleges/northland-international-university/', 'https://www.niche.com/colleges/carolina-college-of-biblical-studies/', 'https://www.niche.com/colleges/universidad-pentecostal-mizpa/', 'https://www.niche.com/colleges/southern-california-university-of-health-sciences/', 'https://www.niche.com/colleges/rio-grande-bible-institute/', 'https://www.niche.com/colleges/antioch-college/', 'https://www.niche.com/colleges/compass-college-of-cinematic-arts/', 'https://www.niche.com/colleges/berkeley-college---paramus/', 'https://www.niche.com/colleges/dewey-university---juana-diaz/', 'https://www.niche.com/colleges/trinity-college-of-nursing--and--health-sciences/', 'https://www.niche.com/colleges/shor-yoshuv-rabbinical-college/', 'https://www.niche.com/colleges/research-college-of-nursing/', 'https://www.niche.com/colleges/national-american-university---austin/', 'https://www.niche.com/colleges/alliant-international-university/', 'https://www.niche.com/colleges/virginia-international-university/', 'https://www.niche.com/colleges/charles-r-drew-university-of-medicine--and--science/', 'https://www.niche.com/colleges/palo-alto-university/', 'https://www.niche.com/colleges/st-lukes-college/', 'https://www.niche.com/colleges/remington-college-of-nursing---orlando/', 'https://www.niche.com/colleges/stevens-henager-college---idaho-falls/', 'https://www.niche.com/colleges/stevens-henager-college---st-george/', 'https://www.niche.com/colleges/aultman-college-of-nursing--and--health-sciences/', 'https://www.niche.com/colleges/columbia-college-of-nursing/', 'https://www.niche.com/colleges/st-johns-college-of-nursing/', 'https://www.niche.com/colleges/bais-medrash-toras-chesed/', 'https://www.niche.com/colleges/charlotte-christian-college-and-theological-seminary/', 'https://www.niche.com/colleges/criswell-college/', 'https://www.niche.com/colleges/mid-america-college-of-funeral-service/', 'https://www.niche.com/colleges/national-graduate-school-of-quality-management/', 'https://www.niche.com/colleges/ohr-hameir-theological-seminary/', 'https://www.niche.com/colleges/strayer-university---new-jersey/', 'https://www.niche.com/colleges/centura-college---virginia-beach/', 'https://www.niche.com/colleges/united-states-university/', 'https://www.niche.com/colleges/good-samaritan-college-of-nursing--and--health-science/', 'https://www.niche.com/colleges/universidad-central-del-caribe/', 'https://www.niche.com/colleges/webb-institute/', 'https://www.niche.com/colleges/minnesota-school-of-business---waite-park/', 'https://www.niche.com/colleges/sanford-college-of-nursing/', 'https://www.niche.com/colleges/yeshiva-shaarei-torah-of-rockland/', 'https://www.niche.com/colleges/homestead-schools/', 'https://www.niche.com/colleges/central-baptist-theological-seminary/', 'https://www.niche.com/colleges/pontifical-college-josephinum/', 'https://www.niche.com/colleges/thomas-more-college-of-liberal-arts/', 'https://www.niche.com/colleges/faith-evangelical-college--and--seminary/', 'https://www.niche.com/colleges/pacific-rim-christian-university/', 'https://www.niche.com/colleges/averett-university---non-traditional-programs/', 'https://www.niche.com/colleges/antioch-university---los-angeles/', 'https://www.niche.com/colleges/crossroads-college/', 'https://www.niche.com/colleges/rabbi-jacob-joseph-school---adult-education/', 'https://www.niche.com/colleges/ottawa-university---online/', 'https://www.niche.com/colleges/aspen-university/', 'https://www.niche.com/colleges/ottawa-university---milwaukee/', 'https://www.niche.com/colleges/millennia-atlantic-university/', 'https://www.niche.com/colleges/northwest-college-of-art--and--design/', 'https://www.niche.com/colleges/yeshiva-derech-chaim/', 'https://www.niche.com/colleges/yeshiva-shaar-hatorah---adult-education/', 'https://www.niche.com/colleges/national-american-university---overland-park/', 'https://www.niche.com/colleges/american-sentinel-university/', 'https://www.niche.com/colleges/design-institute-of-san-diego/', 'https://www.niche.com/colleges/southeast-missouri-hospital-college-of-nursing--and--health-sciences/', 'https://www.niche.com/colleges/pacific-college-of-oriental-medicine---san-diego/', 'https://www.niche.com/colleges/chamberlain-college-of-nursing---indianapolis/', 'https://www.niche.com/colleges/hellenic-college--and--holy-cross-greek-orthodox-school-of-theology/', 'https://www.niche.com/colleges/walsh-college-of-accountancy--and--business-administration/', 'https://www.niche.com/colleges/bais-hamedrash--and--mesivta-of-baltimore/', 'https://www.niche.com/colleges/lynchburg-general-hospital-school-of-nursing/', 'https://www.niche.com/colleges/minnesota-school-of-business---shakopee/', 'https://www.niche.com/colleges/nazarene-bible-college/', 'https://www.niche.com/colleges/american-indian-college-of-the-assemblies-of-god/', 'https://www.niche.com/colleges/the-north-coast-college/', 'https://www.niche.com/colleges/pacific-college-of-oriental-medicine---new-york/', 'https://www.niche.com/colleges/strayer-university---alabama/', 'https://www.niche.com/colleges/lincoln-university---california/', 'https://www.niche.com/colleges/stevens-henager-college---logan/', 'https://www.niche.com/colleges/divine-word-college/', 'https://www.niche.com/colleges/northeast-catholic-college/', 'https://www.niche.com/colleges/yeshiva-dmonsey-rabbinical-college/', 'https://www.niche.com/colleges/lyme-academy-college-of-fine-arts/', 'https://www.niche.com/colleges/allegheny-wesleyan-college/', 'https://www.niche.com/colleges/grace-college-of-divinity/', 'https://www.niche.com/colleges/iglobal-university/', 'https://www.niche.com/colleges/conception-seminary-college/', 'https://www.niche.com/colleges/new-hope-christian-college/', 'https://www.niche.com/colleges/rush-university/', 'https://www.niche.com/colleges/saint-charles-borromeo-seminary/', 'https://www.niche.com/colleges/college-of-biblical-studies---houston/', 'https://www.niche.com/colleges/minnesota-school-of-business---moorhead/', 'https://www.niche.com/colleges/national-american-university---albuquerque/', 'https://www.niche.com/colleges/torah-temimah-talmudical-seminary/', 'https://www.niche.com/colleges/devry-university---missouri/', 'https://www.niche.com/colleges/kentucky-mountain-bible-college/', 'https://www.niche.com/colleges/telshe-yeshiva---chicago/', 'https://www.niche.com/colleges/holy-apostles-college--and--seminary/', 'https://www.niche.com/colleges/saint-louis-christian-college/', 'https://www.niche.com/colleges/trinity-international-university---davie/', 'https://www.niche.com/colleges/clear-creek-baptist-bible-college/', 'https://www.niche.com/colleges/interior-designers-institute/', 'https://www.niche.com/colleges/thomas-edison-state-university/', 'https://www.niche.com/colleges/northwestern-health-sciences-university/', 'https://www.niche.com/colleges/key-college/', 'https://www.niche.com/colleges/national-american-university---centennial/', 'https://www.niche.com/colleges/southwest-university-of-visual-arts---albuquerque/', 'https://www.niche.com/colleges/talmudical-academy---new-jersey/', 'https://www.niche.com/colleges/yeshiva-gedolah-of-greater-detroit/', 'https://www.niche.com/colleges/antioch-university---santa-barbara/', 'https://www.niche.com/colleges/boston-baptist-college/', 'https://www.niche.com/colleges/broadview-entertainment-arts-university/', 'https://www.niche.com/colleges/national-american-university---colorado-springs-south/', 'https://www.niche.com/colleges/sacred-heart-major-seminary/', 'https://www.niche.com/colleges/luther-rice-college--and--seminary/', 'https://www.niche.com/colleges/st-john-vianney-college-seminary/', 'https://www.niche.com/colleges/beth-hamedrash-shaarei-yosher-institute/', 'https://www.niche.com/colleges/national-american-university---colorado-springs/', 'https://www.niche.com/colleges/phillips-beth-israel-school-of-nursing/', 'https://www.niche.com/colleges/world-mission-university/', 'https://www.niche.com/colleges/mount-angel-seminary/', 'https://www.niche.com/colleges/polytechnic-university-of-puerto-rico---orlando/', 'https://www.niche.com/colleges/south-baylo-university/', 'https://www.niche.com/colleges/devry-university---north-carolina/', 'https://www.niche.com/colleges/bryant--and--stratton-college---akron/', 'https://www.niche.com/colleges/devry-university---nevada/', 'https://www.niche.com/colleges/ilisagvik-college/', 'https://www.niche.com/colleges/logan-university/', 'https://www.niche.com/colleges/national-american-university---ellsworth-afb-extension/', 'https://www.niche.com/colleges/new-york-college-of-traditional-chinese-medicine/', 'https://www.niche.com/colleges/mesivtha-tifereth-jerusalem-of-america/', 'https://www.niche.com/colleges/montana-bible-college/', 'https://www.niche.com/colleges/hussian-college/', 'https://www.niche.com/colleges/international-baptist-college/', 'https://www.niche.com/colleges/kenrick-glennon-seminary/', 'https://www.niche.com/colleges/paier-college-of-art/', 'https://www.niche.com/colleges/the-creative-center/', 'https://www.niche.com/colleges/west-virginia-university-hospital---departments-of-rad-tech--and--nutrition/', 'https://www.niche.com/colleges/california-institute-of-integral-studies/', 'https://www.niche.com/colleges/john-f-kennedy-university/', 'https://www.niche.com/colleges/gratz-college/', 'https://www.niche.com/colleges/academy-college/', 'https://www.niche.com/colleges/national-american-university---albuquerque-west/', 'https://www.niche.com/colleges/longy-school-of-music-of-bard-college/', 'https://www.niche.com/colleges/university-of-phoenix---puerto-rico/', 'https://www.niche.com/colleges/atlantic-institute-of-oriental-medicine/', 'https://www.niche.com/colleges/yeshivas-beer-yitzchok/', 'https://www.niche.com/colleges/pacific-islands-university/', 'https://www.niche.com/colleges/bergin-university-of-canine-studies/', 'https://www.niche.com/colleges/hebrew-college/', 'https://www.niche.com/colleges/messenger-college/', 'https://www.niche.com/colleges/city-vision-university/', 'https://www.niche.com/colleges/palmer-college-of-chiropractic---davenport/', 'https://www.niche.com/colleges/rabbinical-college-beth-shraga/', 'https://www.niche.com/colleges/bais-medrash-elyon/', 'https://www.niche.com/colleges/national-university-of-natural-medicine/', 'https://www.niche.com/colleges/whitworth-university---adult-degree-programs/', 'https://www.niche.com/colleges/williamson-christian-college/', 'https://www.niche.com/colleges/acupuncture--and--massage-college/', 'https://www.niche.com/colleges/carver-college/', 'https://www.niche.com/colleges/national-american-university---sioux-falls/', 'https://www.niche.com/colleges/rabbinical-college-telshe/', 'https://www.niche.com/colleges/san-juan-bautista-school-of-medicine/', 'https://www.niche.com/colleges/university-of-the-potomac---vienna/', 'https://www.niche.com/colleges/laboure-college/', 'https://www.niche.com/colleges/national-university-of-health-sciences/', 'https://www.niche.com/colleges/ottawa-university---jeffersonville/', 'https://www.niche.com/colleges/daymar-college---paducah-main/', 'https://www.niche.com/colleges/mesivta-keser-torah---adult-education/', 'https://www.niche.com/colleges/pacific-college-of-oriental-medicine---chicago/', 'https://www.niche.com/colleges/yeshivath-beth-moshe/', 'https://www.niche.com/colleges/devry-university---tennessee/', 'https://www.niche.com/colleges/purdue-university-global---mason-city-campus/', 'https://www.niche.com/colleges/carolina-christian-college/', 'https://www.niche.com/colleges/collegeamerica---south-colorado-springs/', 'https://www.niche.com/colleges/talmudic-college-of-florida/', 'https://www.niche.com/colleges/mesivta-of-eastern-parkway---yeshiva-zichron-meilech/', 'https://www.niche.com/colleges/cleveland-university---kansas-city/', 'https://www.niche.com/colleges/alaska-bible-college/', 'https://www.niche.com/colleges/epic-bible-college/', 'https://www.niche.com/colleges/national-american-university---zona-rosa/', 'https://www.niche.com/colleges/duluth-business-university/', 'https://www.niche.com/colleges/national-american-university---lees-summit/', 'https://www.niche.com/colleges/strayer-university---delaware/', 'https://www.niche.com/colleges/amberton-university/', 'https://www.niche.com/colleges/deep-springs-college/', 'https://www.niche.com/colleges/heritage-christian-university/', 'https://www.niche.com/colleges/louisiana-state-university-health-sciences-center---shreveport/', 'https://www.niche.com/colleges/saint-johns-seminary---massachusetts/', 'https://www.niche.com/colleges/bais-binyomin-academy/', 'https://www.niche.com/colleges/christian-life-college/', 'https://www.niche.com/colleges/heritage-bible-college/', 'https://www.niche.com/colleges/national-american-university---mesquite/', 'https://www.niche.com/colleges/yeshiva-college-of-the-nations-capital/', 'https://www.niche.com/colleges/st-vincents-college---connecticut/', 'https://www.niche.com/colleges/yeshivah-gedolah-rabbinical-college/', 'https://www.niche.com/colleges/yeshivat-mikdash-melech/', 'https://www.niche.com/colleges/shasta-bible-college--and--graduate-school/', 'https://www.niche.com/colleges/american-college-of-healthcare-sciences/', 'https://www.niche.com/colleges/dongguk-university/', 'https://www.niche.com/colleges/national-american-university---independence/', 'https://www.niche.com/colleges/polytechnic-university-of-puerto-rico---miami/', 'https://www.niche.com/colleges/university-of-phoenix---boston/', 'https://www.niche.com/colleges/devry-university---indiana/', 'https://www.niche.com/colleges/yeshiva-gedolah-zichron-leyma/', 'https://www.niche.com/colleges/antioch-university---midwest/', 'https://www.niche.com/colleges/national-american-university---brooklyn-center/', 'https://www.niche.com/colleges/notre-dame-seminary-graduate-school-of-theology/', 'https://www.niche.com/colleges/rabbinical-college-of-chsan-sofer-new-york/', 'https://www.niche.com/colleges/abraham-lincoln-university/', 'https://www.niche.com/colleges/dellarte-international-school-of-physical-theatre/', 'https://www.niche.com/colleges/long-island-university---riverhead/', 'https://www.niche.com/colleges/strayer-university---west-virginia/', 'https://www.niche.com/colleges/university-of-phoenix---indianapolis/', 'https://www.niche.com/colleges/birthingway-college-of-midwifery/', 'https://www.niche.com/colleges/gemini-school-of-visual-arts/', 'https://www.niche.com/colleges/georgia-central-university/', 'https://www.niche.com/colleges/southeastern-baptist-college/', 'https://www.niche.com/colleges/the-art-institute-of-cincinnati---aic-college-of-design/', 'https://www.niche.com/colleges/touro-university---nevada/', 'https://www.niche.com/colleges/university-of-phoenix---louisville/', 'https://www.niche.com/colleges/antioch-university---seattle/', 'https://www.niche.com/colleges/bethel-college---virginia/', 'https://www.niche.com/colleges/national-american-university---tulsa/', 'https://www.niche.com/colleges/pentecostal-theological-seminary/', 'https://www.niche.com/colleges/summit-christian-college/', 'https://www.niche.com/colleges/texas-health-and-science-university/', 'https://www.niche.com/colleges/huntsville-bible-college/', 'https://www.niche.com/colleges/linfield-college---adult-degree-program/', 'https://www.niche.com/colleges/montessori-education-center-of-the-rockies/', 'https://www.niche.com/colleges/cooper-health-system-center-for-allied-health-education/', 'https://www.niche.com/colleges/united-states-sports-academy/', 'https://www.niche.com/colleges/los-angeles-academy-of-figurative-art/', 'https://www.niche.com/colleges/national-american-university---roseville/', 'https://www.niche.com/colleges/northcentral-university/', 'https://www.niche.com/colleges/university-of-phoenix---birmingham/', 'https://www.niche.com/colleges/american-conservatory-theater/', 'https://www.niche.com/colleges/baptist-missionary-association-theological-seminary/', 'https://www.niche.com/colleges/family-of-faith-christian-university/', 'https://www.niche.com/colleges/middlebury-institute-for-international-studies-at-monterey/', 'https://www.niche.com/colleges/yeshiva--and--kollel-harbotzas-torah/', 'https://www.niche.com/colleges/globe-university---minneapolis/', 'https://www.niche.com/colleges/ponce-school-of-medicine--and--health-sciences/', 'https://www.niche.com/colleges/southern-california-seminary/', 'https://www.niche.com/colleges/strayer-university---arkansas/', 'https://www.niche.com/colleges/yeshiva-toras-chaim-of-denver/', 'https://www.niche.com/colleges/beth-hatalmud-rabbinical-college/', 'https://www.niche.com/colleges/beverly-hills-design-institute/', 'https://www.niche.com/colleges/eastern-school-of-acupuncture--and--traditional-medicine/', 'https://www.niche.com/colleges/midwest-college-of-oriental-medicine---chicago/', 'https://www.niche.com/colleges/national-american-university---bloomington/', 'https://www.niche.com/colleges/university-of-fort-lauderdale/', 'https://www.niche.com/colleges/university-of-phoenix---milwaukee/', 'https://www.niche.com/colleges/midwest-college-of-oriental-medicine---racine/', 'https://www.niche.com/colleges/american-college-of-education/', 'https://www.niche.com/colleges/talmudical-institute-of-upstate-new-york/', 'https://www.niche.com/colleges/tri-state-bible-college/', 'https://www.niche.com/colleges/california-university-of-management--and--sciences/', 'https://www.niche.com/colleges/pacific-states-university/', 'https://www.niche.com/colleges/taft-university-system/', 'https://www.niche.com/colleges/california-christian-college/', 'https://www.niche.com/colleges/national-american-university---burnsville/', 'https://www.niche.com/colleges/national-american-university---wichita/', 'https://www.niche.com/colleges/strayer-university---mississippi/', 'https://www.niche.com/colleges/cbt-college---kendall/', 'https://www.niche.com/colleges/daymar-college---owensboro/', 'https://www.niche.com/colleges/national-american-university---bellevue/', 'https://www.niche.com/colleges/sofia-university/', 'https://www.niche.com/colleges/austin-graduate-school-of-theology/', 'https://www.niche.com/colleges/jose-maria-vargas-university/', 'https://www.niche.com/colleges/shiloh-university/', 'https://www.niche.com/colleges/devry-university---oklahoma/', 'https://www.niche.com/colleges/trinity-vocational-center/', 'https://www.niche.com/colleges/horizon-university/', 'https://www.niche.com/colleges/the-chicago-school-of-professional-psychology---los-angeles/', 'https://www.niche.com/colleges/w-l-bonner-college/', 'https://www.niche.com/colleges/at-still-university-of-health-sciences/', 'https://www.niche.com/colleges/aoma-graduate-school-of-integrative-medicine/', 'https://www.niche.com/colleges/academy-for-five-element-acupuncture/', 'https://www.niche.com/colleges/academy-for-jewish-religion---california/', 'https://www.niche.com/colleges/academy-of-chinese-culture--and--health-sciences/', 'https://www.niche.com/colleges/academy-of-vocal-arts/', 'https://www.niche.com/colleges/acupuncture--and--integrative-medicine-college---berkeley/', 'https://www.niche.com/colleges/adler-graduate-school/', 'https://www.niche.com/colleges/adler-school-of-professional-psychology/', 'https://www.niche.com/colleges/air-force-institute-of-technology---graduate-school-of-engineering--and--management/', 'https://www.niche.com/colleges/albany-law-school/', 'https://www.niche.com/colleges/albany-medical-college/', 'https://www.niche.com/colleges/american-academy-of-acupuncture--and--oriental-medicine/', 'https://www.niche.com/colleges/american-baptist-seminary-of-the-west/', 'https://www.niche.com/colleges/american-college/', 'https://www.niche.com/colleges/american-college-of-acupuncture--and--oriental-medicine/', 'https://www.niche.com/colleges/american-film-institute-conservatory/', 'https://www.niche.com/colleges/anabaptist-mennonite-biblical-seminary/', 'https://www.niche.com/colleges/andover-newton-theological-school/', 'https://www.niche.com/colleges/antioch-university/', 'https://www.niche.com/colleges/antioch-university---new-england/', 'https://www.niche.com/colleges/antioch-university-phd-program-in-leadership--and--change/', 'https://www.niche.com/colleges/appalachian-college-of-pharmacy/', 'https://www.niche.com/colleges/appalachian-school-of-law/', 'https://www.niche.com/colleges/aquinas-institute-of-theology/', 'https://www.niche.com/colleges/arizona-school-of-acupuncture--and--oriental-medicine/', 'https://www.niche.com/colleges/arizona-summit-law-school/', 'https://www.niche.com/colleges/asbury-theological-seminary/', 'https://www.niche.com/colleges/assemblies-of-god-theological-seminary/', 'https://www.niche.com/colleges/athenaeum-of-ohio/', 'https://www.niche.com/colleges/athens-college-of-ministry/', 'https://www.niche.com/colleges/austin-presbyterian-theological-seminary/', 'https://www.niche.com/colleges/ave-maria-school-of-law/', 'https://www.niche.com/colleges/bainbridge-graduate-institute/', 'https://www.niche.com/colleges/bakke-graduate-university/', 'https://www.niche.com/colleges/bank-street-college-of-education/', 'https://www.niche.com/colleges/baptist-theological-seminary-at-richmond/', 'https://www.niche.com/colleges/bath-spa-university/', 'https://www.niche.com/colleges/baylor-college-of-medicine/', 'https://www.niche.com/colleges/bethany-theological-seminary/', 'https://www.niche.com/colleges/bethel-seminary---st-paul/', 'https://www.niche.com/colleges/bethel-university/', 'https://www.niche.com/colleges/bexley-hall-episcopal-seminary/', 'https://www.niche.com/colleges/biblical-theological-seminary/', 'https://www.niche.com/colleges/blessed-john-xxiii-national-seminary/', 'https://www.niche.com/colleges/boston-graduate-school-of-psychoanalysis/', 'https://www.niche.com/colleges/brite-divinity-school/', 'https://www.niche.com/colleges/brooklyn-law-school/', 'https://www.niche.com/colleges/byzantine-catholic-seminary/', 'https://www.niche.com/colleges/cuny-school-of-law-at-queens-college/', 'https://www.niche.com/colleges/california-coast-university/', 'https://www.niche.com/colleges/california-western-school-of-law/', 'https://www.niche.com/colleges/calvin-theological-seminary/', 'https://www.niche.com/colleges/catholic-theological-union-at-chicago/', 'https://www.niche.com/colleges/center-for-advanced-studies-on-puerto-rico--and--the-caribbean/', 'https://www.niche.com/colleges/chamberlain-college-of-nursing/', 'https://www.niche.com/colleges/charleston-school-of-law/', 'https://www.niche.com/colleges/chicago-theological-seminary/', 'https://www.niche.com/colleges/christ-the-king-seminary/', 'https://www.niche.com/colleges/christian-theological-seminary/', 'https://www.niche.com/colleges/christies-education/', 'https://www.niche.com/colleges/church-divinity-school-of-the-pacific/', 'https://www.niche.com/colleges/claremont-graduate-university/', 'https://www.niche.com/colleges/claremont-school-of-theology/', 'https://www.niche.com/colleges/colgate-rochester-crozer-divinity-school/', 'https://www.niche.com/colleges/colorado-school-of-traditional-chinese-medicine/', 'https://www.niche.com/colleges/columbia-theological-seminary/', 'https://www.niche.com/colleges/concordia-seminary/', 'https://www.niche.com/colleges/concordia-theological-seminary/', 'https://www.niche.com/colleges/conway-school-of-landscape-design/', 'https://www.niche.com/colleges/covenant-theological-seminary/', 'https://www.niche.com/colleges/dallas-theological-seminary/', 'https://www.niche.com/colleges/daoist-traditions-college-of-chinese-medical-arts/', 'https://www.niche.com/colleges/devry-university/', 'https://www.niche.com/colleges/delaware-technical-community-college/', 'https://www.niche.com/colleges/denver-seminary/', 'https://www.niche.com/colleges/des-moines-university---osteopathic-medical-center/', 'https://www.niche.com/colleges/dharma-realm-buddhist-university/', 'https://www.niche.com/colleges/dominican-school-of-philosophy--and--theology/', 'https://www.niche.com/colleges/dragon-rises-college-of-oriental-medicine/', 'https://www.niche.com/colleges/eastern-virginia-medical-school/', 'https://www.niche.com/colleges/ecumenical-theological-seminary/', 'https://www.niche.com/colleges/eden-theological-seminary/', 'https://www.niche.com/colleges/edward-via-college-of-osteopathic-medicine/', 'https://www.niche.com/colleges/elizabethtown-college-school-of-continuing--and--professional-studies/', 'https://www.niche.com/colleges/emperors-college-of-traditional-oriental-medicine/', 'https://www.niche.com/colleges/episcopal-theological-seminary-of-the-southwest/', 'https://www.niche.com/colleges/erikson-institute/', 'https://www.niche.com/colleges/evangelical-theological-seminary/', 'https://www.niche.com/colleges/excelsior-college/', 'https://www.niche.com/colleges/fielding-graduate-university/', 'https://www.niche.com/colleges/five-branches-university/', 'https://www.niche.com/colleges/florida-coastal-school-of-law/', 'https://www.niche.com/colleges/florida-college-of-integrative-medicine/', 'https://www.niche.com/colleges/foothill-de-anza-community-colleges/', 'https://www.niche.com/colleges/franciscan-school-of-theology/', 'https://www.niche.com/colleges/frontier-nursing-university/', 'https://www.niche.com/colleges/fuller-theological-seminary-in-california/', 'https://www.niche.com/colleges/garrett-evangelical-theological-seminary/', 'https://www.niche.com/colleges/gordon-conwell-theological-seminary/', 'https://www.niche.com/colleges/graduate-theological-union/', 'https://www.niche.com/colleges/hartford-seminary/', 'https://www.niche.com/colleges/hazelden-graduate-school-of-addiction-studies/', 'https://www.niche.com/colleges/hebrew-union-college---jewish-institute-of-religion/', 'https://www.niche.com/colleges/hood-theological-seminary/', 'https://www.niche.com/colleges/houston-graduate-school-of-theology/', 'https://www.niche.com/colleges/icahn-school-of-medicine-at-mount-sinai/', 'https://www.niche.com/colleges/iliff-school-of-theology/', 'https://www.niche.com/colleges/illinois-college-of-optometry/', 'https://www.niche.com/colleges/institute-for-clinical-social-work/', 'https://www.niche.com/colleges/institute-for-doctoral-studies-in-the-visual-arts/', 'https://www.niche.com/colleges/institute-for-the-psychological-sciences/', 'https://www.niche.com/colleges/institute-of-clinical-acupuncture--and--oriental-med/', 'https://www.niche.com/colleges/institute-of-taoist-education--and--acupuncture/', 'https://www.niche.com/colleges/institute-of-world-politics/', 'https://www.niche.com/colleges/inter-american-university-of-puerto-rico---school-of-law/', 'https://www.niche.com/colleges/inter-american-university-of-puerto-rico---school-of-optometry/', 'https://www.niche.com/colleges/interdenominational-theological-center/', 'https://www.niche.com/colleges/international-institute-for-restorative-practices/', 'https://www.niche.com/colleges/international-technological-university/', 'https://www.niche.com/colleges/irell--and--manella-graduate-school-of-biological-sciences/', 'https://www.niche.com/colleges/john-marshall-law-school---atlanta/', 'https://www.niche.com/colleges/jung-tao-school-of-classical-chinese-medicine/', 'https://www.niche.com/colleges/kansas-city-university-of-medicine--and--biosciences/', 'https://www.niche.com/colleges/keck-graduate-institute/', 'https://www.niche.com/colleges/lake-erie-college-of-osteopathic-medicine/', 'https://www.niche.com/colleges/lake-forest-graduate-school-of-management/', 'https://www.niche.com/colleges/lancaster-theological-seminary/', 'https://www.niche.com/colleges/lester-e-cox-medical-center---school-of-medical-technology/', 'https://www.niche.com/colleges/lexington-theological-seminary/', 'https://www.niche.com/colleges/life-chiropractic-college---west/', 'https://www.niche.com/colleges/long-island-university---brentwood/', 'https://www.niche.com/colleges/long-island-university---rockland/', 'https://www.niche.com/colleges/long-island-university---westchester/', 'https://www.niche.com/colleges/louisville-presbyterian-theological-seminary/', 'https://www.niche.com/colleges/luther-seminary/', 'https://www.niche.com/colleges/lutheran-school-of-theology-at-chicago/', 'https://www.niche.com/colleges/lutheran-theological-seminary-at-gettysburg/', 'https://www.niche.com/colleges/lutheran-theological-seminary-at-philadelphia/', 'https://www.niche.com/colleges/maple-springs-baptist-bible-college--and--seminary/', 'https://www.niche.com/colleges/marlboro-college-graduate-school/', 'https://www.niche.com/colleges/maryland-university-of-integrative-health/', 'https://www.niche.com/colleges/massachusetts-general-hospital-dietetic-internship/', 'https://www.niche.com/colleges/massachusetts-school-of-law/', 'https://www.niche.com/colleges/mayo-graduate-school/', 'https://www.niche.com/colleges/mayo-medical-school/', 'https://www.niche.com/colleges/mccormick-theological-seminary/', 'https://www.niche.com/colleges/meadville-lombard-theological-school/', 'https://www.niche.com/colleges/medical-college-of-wisconsin/', 'https://www.niche.com/colleges/meharry-medical-college/', 'https://www.niche.com/colleges/memphis-theological-seminary/', 'https://www.niche.com/colleges/methodist-theological-school-in-ohio/', 'https://www.niche.com/colleges/michigan-school-of-professional-psychology/', 'https://www.niche.com/colleges/michigan-state-university-college-of-law/', 'https://www.niche.com/colleges/middle-tennessee-school-of-anesthesia/', 'https://www.niche.com/colleges/midwestern-university---downers-grove/', 'https://www.niche.com/colleges/midwestern-university---glendale-az/', 'https://www.niche.com/colleges/montessori-institute-of-milwaukee/', 'https://www.niche.com/colleges/morehouse-school-of-medicine/', 'https://www.niche.com/colleges/nashotah-house/', 'https://www.niche.com/colleges/naval-postgraduate-school/', 'https://www.niche.com/colleges/nazarene-theological-seminary/', 'https://www.niche.com/colleges/new-brunswick-theological-seminary/', 'https://www.niche.com/colleges/new-england-college-of-optometry/', 'https://www.niche.com/colleges/new-england-law---boston/', 'https://www.niche.com/colleges/new-york-academy-of-art/', 'https://www.niche.com/colleges/new-york-chiropractic-college/', 'https://www.niche.com/colleges/new-york-college-of-podiatric-medicine/', 'https://www.niche.com/colleges/new-york-film-academy-south-beach/', 'https://www.niche.com/colleges/new-york-law-school/', 'https://www.niche.com/colleges/new-york-medical-college/', 'https://www.niche.com/colleges/new-york-theological-seminary/', 'https://www.niche.com/colleges/north-orange-county-community-colleges/', 'https://www.niche.com/colleges/northshore-university-healthsystem-school-of-nurse-anesthesia/', 'https://www.niche.com/colleges/northeast-ohio-medical-university/', 'https://www.niche.com/colleges/northeastern-seminary/', 'https://www.niche.com/colleges/northern-baptist-theological-seminary/', 'https://www.niche.com/colleges/oblate-school-of-theology/', 'https://www.niche.com/colleges/oklahoma-state-university---center-for-health-sciences/', 'https://www.niche.com/colleges/omega-graduate-school/', 'https://www.niche.com/colleges/oregon-college-of-oriental-medicine/', 'https://www.niche.com/colleges/pacific-northwest-university-of-health-sciences/', 'https://www.niche.com/colleges/pacific-oaks-college/', 'https://www.niche.com/colleges/pacific-school-of-religion/', 'https://www.niche.com/colleges/pacifica-graduate-institute/', 'https://www.niche.com/colleges/pardee-rand-graduate-school/', 'https://www.niche.com/colleges/parsons-paris---the-new-school/', 'https://www.niche.com/colleges/payne-theological-seminary/', 'https://www.niche.com/colleges/penn-state-college-of-medicine/', 'https://www.niche.com/colleges/penn-state-great-valley/', 'https://www.niche.com/colleges/philadelphia-college-of-osteopathic-medicine/', 'https://www.niche.com/colleges/phillips-graduate-university/', 'https://www.niche.com/colleges/phillips-theological-seminary/', 'https://www.niche.com/colleges/phoenix-institute-of-herbal-medicine--and--acupuncture/', 'https://www.niche.com/colleges/phoenix-seminary/', 'https://www.niche.com/colleges/pittsburgh-theological-seminary/', 'https://www.niche.com/colleges/pontifical-faculty-of-the-immaculate-conception-at-the-dominican-house-of-studies/', 'https://www.niche.com/colleges/pontifical-john-paul-ii-institute-for-studies-on-marriage--and--family/', 'https://www.niche.com/colleges/princeton-theological-seminary/', 'https://www.niche.com/colleges/quest-university-canada/', 'https://www.niche.com/colleges/rasmussen-college---aurora/', 'https://www.niche.com/colleges/rasmussen-college---blaine/', 'https://www.niche.com/colleges/rasmussen-college---fort-myers/', 'https://www.niche.com/colleges/rasmussen-college---kansas-city-overland-park/', 'https://www.niche.com/colleges/rasmussen-college---land-olakes-east-pasco/', 'https://www.niche.com/colleges/rasmussen-college---mokena-tinley-park/', 'https://www.niche.com/colleges/rasmussen-college---moorhead/', 'https://www.niche.com/colleges/rasmussen-college---new-port-richey/', 'https://www.niche.com/colleges/rasmussen-college---romeoville-joliet/', 'https://www.niche.com/colleges/rasmussen-college---tampa-brandon/', 'https://www.niche.com/colleges/rasmussen-college---topeka/', 'https://www.niche.com/colleges/rasmussen-college---wausau/', 'https://www.niche.com/colleges/reconstructionist-rabbinical-college/', 'https://www.niche.com/colleges/reformed-presbyterian-theological-seminary/', 'https://www.niche.com/colleges/relay-graduate-school-of-education/', 'https://www.niche.com/colleges/rensselaer-hartford-graduate-center/', 'https://www.niche.com/colleges/richmond---the-american-international-university-in-london/', 'https://www.niche.com/colleges/richmont-graduate-university/', 'https://www.niche.com/colleges/rockefeller-university/', 'https://www.niche.com/colleges/rocky-mountain-university-of-health-professions/', 'https://www.niche.com/colleges/roger-williams-university-school-of-law/', 'https://www.niche.com/colleges/rosalind-franklin-university-of-medicine--and--science/', 'https://www.niche.com/colleges/sit-graduate-institute/', 'https://www.niche.com/colleges/suny-college-of-optometry/', 'https://www.niche.com/colleges/sacred-heart-school-of-theology/', 'https://www.niche.com/colleges/saint-meinrad-school-of-theology/', 'https://www.niche.com/colleges/saint-paul-school-of-theology/', 'https://www.niche.com/colleges/saint-vincent-seminary/', 'https://www.niche.com/colleges/salus-university/', 'https://www.niche.com/colleges/san-francisco-theological-seminary/', 'https://www.niche.com/colleges/san-joaquin-college-of-law/', 'https://www.niche.com/colleges/san-joaquin-valley-college/', 'https://www.niche.com/colleges/san-mateo-county-community-colleges/', 'https://www.niche.com/colleges/saybrook-university/', 'https://www.niche.com/colleges/seattle-institute-of-oriental-medicine/', 'https://www.niche.com/colleges/seminario-evangelico-de-puerto-rico/', 'https://www.niche.com/colleges/shepherds-theological-seminary/', 'https://www.niche.com/colleges/sherman-college/', 'https://www.niche.com/colleges/sioux-falls-seminary/', 'https://www.niche.com/colleges/south-texas-college-of-law/', 'https://www.niche.com/colleges/southern-california-college-of-optometry/', 'https://www.niche.com/colleges/southern-california-university-soma/', 'https://www.niche.com/colleges/southern-college-of-optometry/', 'https://www.niche.com/colleges/southern-university-law-center/', 'https://www.niche.com/colleges/southwest-acupuncture-college---boulder/', 'https://www.niche.com/colleges/southwest-acupuncture-college---santa-fe/', 'https://www.niche.com/colleges/southwest-college-of-naturopathic-medicine--and--health-sciences/', 'https://www.niche.com/colleges/southwestern-college---new-mexico/', 'https://www.niche.com/colleges/southwestern-law-school/', 'https://www.niche.com/colleges/spertus-college/', 'https://www.niche.com/colleges/st-bernards-school-of-theology--and--ministry/', 'https://www.niche.com/colleges/st-johns-seminary---california/', 'https://www.niche.com/colleges/st-vincent-de-paul-regional-seminary/', 'https://www.niche.com/colleges/st-vladimirs-orthodox-theological-seminary/', 'https://www.niche.com/colleges/starr-king-school-for-ministry/', 'https://www.niche.com/colleges/taliesin---frank-lloyd-wright-school-of-architecture/', 'https://www.niche.com/colleges/teachers-college-at-columbia-university/', 'https://www.niche.com/colleges/texas-chiropractic-college-foundation/', 'https://www.niche.com/colleges/the-chicago-school-of-professional-psychology---chicago/', 'https://www.niche.com/colleges/the-chicago-school-of-professional-psychology---irvine/', 'https://www.niche.com/colleges/the-chicago-school-of-professional-psychology---washington-dc/', 'https://www.niche.com/colleges/the-commonwealth-medical-college/', 'https://www.niche.com/colleges/the-dickinson-school-of-law-of-the-pennsylvania-state-university/', 'https://www.niche.com/colleges/the-general-theological-seminary/', 'https://www.niche.com/colleges/the-john-marshall-law-school/', 'https://www.niche.com/colleges/the-santa-barbara--and--ventura-colleges-of-law---santa-barbara/', 'https://www.niche.com/colleges/the-santa-barbara--and--ventura-colleges-of-law---ventura/', 'https://www.niche.com/colleges/the-seattle-school-of-theology--and--psychology/', 'https://www.niche.com/colleges/the-university-of-america/', 'https://www.niche.com/colleges/the-wright-institute/', 'https://www.niche.com/colleges/theological-seminary-of-the-reformed-episcopal-church/', 'https://www.niche.com/colleges/thomas-jefferson-school-of-law/', 'https://www.niche.com/colleges/thomas-m-cooley-law-school/', 'https://www.niche.com/colleges/thunderbird-school-of-global-management/', 'https://www.niche.com/colleges/touro-university---california/', 'https://www.niche.com/colleges/tri-state-college-of-acupuncture/', 'https://www.niche.com/colleges/trinity-law-school/', 'https://www.niche.com/colleges/trinity-lutheran-seminary-at-capital-university/', 'https://www.niche.com/colleges/trinity-school-for-ministry/', 'https://www.niche.com/colleges/unification-theological-seminary/', 'https://www.niche.com/colleges/union-presbyterian-seminary/', 'https://www.niche.com/colleges/union-theological-seminary/', 'https://www.niche.com/colleges/united-theological-seminary/', 'https://www.niche.com/colleges/united-theological-seminary-of-the-twin-cities/', 'https://www.niche.com/colleges/universidad-internacional-iberoamericana/', 'https://www.niche.com/colleges/university-of-california-hastings-college-of-the-law/', 'https://www.niche.com/colleges/university-of-east-west-medicine/', 'https://www.niche.com/colleges/university-of-massachusetts-medical-school-worcester/', 'https://www.niche.com/colleges/university-of-new-hampshire---school-of-law/', 'https://www.niche.com/colleges/university-of-north-texas-health-science-center/', 'https://www.niche.com/colleges/university-of-saint-mary-of-the-lake/', 'https://www.niche.com/colleges/university-of-st-augustine-for-health-sciences/', 'https://www.niche.com/colleges/university-of-texas---southwestern-medical-center/', 'https://www.niche.com/colleges/university-of-western-states/', 'https://www.niche.com/colleges/university-of-wisconsin---extension/', 'https://www.niche.com/colleges/university-of-the-district-of-columbia-david-a-clarke-school-of-law/', 'https://www.niche.com/colleges/upper-valley-educators-institute/', 'https://www.niche.com/colleges/urshan-graduate-school-of-theology/', 'https://www.niche.com/colleges/vermont-college-of-fine-arts/', 'https://www.niche.com/colleges/vermont-law-school/', 'https://www.niche.com/colleges/wartburg-theological-seminary/', 'https://www.niche.com/colleges/weill-cornell-medical-college/', 'https://www.niche.com/colleges/wesley-biblical-seminary/', 'https://www.niche.com/colleges/wesley-theological-seminary/', 'https://www.niche.com/colleges/west-coast-baptist-college/', 'https://www.niche.com/colleges/west-virginia-school-of-osteopathic-medicine/', 'https://www.niche.com/colleges/western-seminary/', 'https://www.niche.com/colleges/western-state-college-of-law/', 'https://www.niche.com/colleges/western-theological-seminary/', 'https://www.niche.com/colleges/western-university-of-health-sciences/', 'https://www.niche.com/colleges/westminster-theological-seminary/', 'https://www.niche.com/colleges/westminster-theological-seminary-in-california/', 'https://www.niche.com/colleges/william-james-college/', 'https://www.niche.com/colleges/william-mitchell-college-of-law/', 'https://www.niche.com/colleges/winebrenner-theological-seminary/', 'https://www.niche.com/colleges/wisconsin-school-of-professional-psychology/', 'https://www.niche.com/colleges/wolford-college/', 'https://www.niche.com/colleges/won-institute-of-graduate-studies/', 'https://www.niche.com/colleges/world-medicine-institute/', 'https://www.niche.com/colleges/yale-new-haven-hospital-dietetic-internship/', 'https://www.niche.com/colleges/yo-san-university-of-traditional-chinese-medicine/', 'https://www.niche.com/colleges/yosemite-community-colleges/']

print(len(urls))

counter = 1
for url in pbar(urls):
	print(counter)
	counter += 1
	my_url = url
	print(my_url)


	# opening connection, grabbing page
	uClient = uReq(my_url)

	#offloads content to a variable
	page_html = uClient.read()

	# closes connection
	uClient.close()

	# html parsing
	page_soup = soup(page_html, "html.parser")

	# name of college
	college_name = page_soup.h1.text
	data[college_name] = {}



	# 'niche report card' or 'niche grade'
	report_card = page_soup.find("div", {"class":"report-card"})
	grades = report_card.findAll("li", {"class":"ordered__list__bucket__item"})
	# dictionary in dictionary for niche report card
	data[college_name]["niche_report_card"] = {}
	for grade in grades:
		grade_label = grade.div.select('div')[0].text
		grade_val = grade.div.select('div')[1].text
		data[college_name]["niche_report_card"][grade_label] = grade_val



	# 'after college'
	after_college = page_soup.find("section", {"id":"after"})
	data[college_name]["after_college"] = {}

	# median earning after 6 years of college
	median_earning_6_years = after_college.find("div", {"class":"profile__bucket--1"}).div.div.div.find("div", {"class":"scalar__value"})
	if (median_earning_6_years != None):
		median_earning_6_years = median_earning_6_years.span.text
	else:
		median_earning_6_years = ''
	data[college_name]["after_college"]["median_earning_6_years"] = median_earning_6_years

	# other after college rates
	other_after_college_rates = after_college.find("div", {"class":"profile__bucket--2"}).div.div.findAll(recursive=False)
	
	# graduation rate
	graduation_rate = other_after_college_rates[0].find("div", {"class":"scalar__value"})
	if (graduation_rate != None):
		graduation_rate = graduation_rate.span.text
	else:
		employment_rate = ''
	data[college_name]["after_college"]["graduation_rate"] = graduation_rate

	# employment rate
	employment_rate = other_after_college_rates[1].find("div", {"class":"scalar__value"})
	if (employment_rate != None):
		employment_rate = employment_rate.span.text
	else:
		employment_rate = ''
	data[college_name]["after_college"]["employment_rate"] = employment_rate
	
	

	# 'students'
	data[college_name]["students"] = {}

	students_enrolled = page_soup.find("section", {"id":"students"}).find("div", {"class":"profile__bucket--1"}).div.div.findAll(recursive=False)
	# full time
	full_time = students_enrolled[0].find("div", {"class":"scalar__value"})
	if (full_time != None):
		full_time = full_time.span.text
	else:
		full_time = ''
	
	# part time
	part_time = students_enrolled[1].find("div", {"class":"scalar__value"})
	if (part_time != None):
		part_time = part_time.span.text
	else:
		part_time = ''
	
	# over 25
	over_25 = students_enrolled[2].find("div", {"class":"scalar__value"})
	if (over_25 != None):
		over_25 = over_25.span.text
	else:
		over_25 = ''
	
	# pell grant
	pell_grant = students_enrolled[3].find("div", {"class":"scalar__value"})
	if (pell_grant != None):
		pell_grant = pell_grant.span.text
	else:
		pell_grant = ''

	# varsity athletes
	varsity_athletes = students_enrolled[4].find("div", {"class":"scalar__value"})
	if (varsity_athletes != None):
		varsity_athletes = varsity_athletes.span.text
	else:
		varsity_athletes = ''

	data[college_name]["students"]["full_time"] = full_time
	data[college_name]["students"]["part_time"] = part_time
	data[college_name]["students"]["over_25"] = over_25
	data[college_name]["students"]["pell_grant"] = pell_grant
	data[college_name]["students"]["varsity_athletes"] = varsity_athletes



	# 'majors'
	data[college_name]["popular_majors"] = []
	majors = page_soup.find("section", {"id":"majors"}).find("ul", {"class":"popular-entities-list"})
	if (majors != None):
		majors = majors.findAll("li")
		for major in majors:
			data[college_name]["popular_majors"].append(major.h6.string)
	else:
		majors = ''

	# 'cost'
	data[college_name]["cost"] = {}
	cost = page_soup.find("section", {"id":"cost"})

	# net price
	net_price = cost.find("div", {"class":"profile__bucket--1"}).find("div", {"class":"scalar__value"})
	if (net_price != None):
		net_price = net_price.span.text
	else:
		net_price = ''
	data[college_name]["cost"]["net_price"] = net_price

	# aid
	aid = cost.find("div", {"class":"profile__bucket--2"}).div.div.findAll(recursive=False)
	average_aid = aid[0].find("div", {"class":"scalar__value"})
	if (average_aid != None):
		average_aid = average_aid.span.text
	else:
		average_aid = ''
	
	percentage_aid = aid[1].find("div", {"class":"scalar__value"})
	if (percentage_aid != None):
		percentage_aid = percentage_aid.span.text
	else:
		percentage_aid = ''

	data[college_name]["cost"]["average_aid"] = average_aid
	data[college_name]["cost"]["percentage_aid"] = percentage_aid






	# 'admissions'
	data[college_name]["admissions"] = {}

	my_url = url + 'admissions'
	print(my_url)
	# opening connection, grabbing page
	uClient = uReq(my_url)
	#offloads content to a variable
	page_html = uClient.read()
	# closes connection
	uClient.close()
	# html parsing
	page_soup = soup(page_html, "html.parser")



	# 'statistics'
	data[college_name]["admissions"]["statistics"] = {}
	
	statistics = page_soup.find("section", {"id":"admissions-statistics"})
	if (statistics !=  None):
		statistics = page_soup.find("section", {"id":"admissions-statistics"}).find("div", {"class":"profile__buckets"})
	else:
		continue

	# acceptance rate
	acceptance_rate = statistics.find("div", {"class":"profile__bucket--1"}).div.div
	if (acceptance_rate.select('div')[2] != None):
		acceptance_rate = acceptance_rate.select('div')[2].span.text
	else:
		acceptance_rate = ''
	data[college_name]["admissions"]["statistics"]["acceptance_rate"] = acceptance_rate

	# early decision acceptance rate
	other_stats =  statistics.find("div", {"class":"profile__bucket--2"}).div.div.findAll(recursive=False)
	early_decision_acceptance_rate = other_stats[0].find("div", {"class":"scalar__value"})
	if (early_decision_acceptance_rate != None):
		data[college_name]["admissions"]["statistics"]["early_decision_acceptance_rate"] = early_decision_acceptance_rate.span.text
	else:
		data[college_name]["admissions"]["statistics"]["early_decision_acceptance_rate"] = ''

	# total applicants
	total_applicants = other_stats[1].find("div", {"class":"scalar__value"})
	if (total_applicants != None):
		data[college_name]["admissions"]["statistics"]["total_applicants"] = total_applicants.span.text
	else:
		data[college_name]["admissions"]["statistics"]["total_applicants"] = ''
	

	# sat 
	sat = statistics.find("div", {"class":"profile__bucket--3"}).div.div.findAll(recursive=False)

	# sat range
	sat_range = sat[0].find("div", {"class":"scalar__value"})
	if (sat_range != None):
		data[college_name]["admissions"]["statistics"]["sat_range"] = sat_range.span.text
	else:
		data[college_name]["admissions"]["statistics"]["sat_range"] = ''

	# sat reading
	sat_reading = sat[1].find("div", {"class":"scalar__value"})
	if (sat_reading != None):
		data[college_name]["admissions"]["statistics"]["sat_reading"] = sat_reading.span.text
	else:
		data[college_name]["admissions"]["statistics"]["sat_reading"] = ''
		
	# sat math
	sat_math = sat[2].find("div", {"class":"scalar__value"})
	if (sat_math != None):
		data[college_name]["admissions"]["statistics"]["sat_math"] = sat_math.span.text
	else:
		data[college_name]["admissions"]["statistics"]["sat_math"] = ''

	# sat submission percentage
	sat_submission_percentage = sat[3].find("div", {"class":"scalar__value"})
	if (sat_submission_percentage != None):
		data[college_name]["admissions"]["statistics"]["sat_submission_percentage"] = sat_submission_percentage.span.text
	else:
		data[college_name]["admissions"]["statistics"]["sat_submission_percentage"] = ''


	# act
	act = statistics.find("div", {"class":"profile__bucket--4"}).div.div.findAll(recursive=False)

	# act range
	act_range = act[0].find("div", {"class":"scalar__value"})
	if (act_range != None):
		data[college_name]["admissions"]["statistics"]["act_range"] = act_range.span.text
	else:
		data[college_name]["admissions"]["statistics"]["act_range"] = ''
	
	# act english
	act_english = act[1].find("div", {"class":"scalar__value"})
	if (act_english != None):
		data[college_name]["admissions"]["statistics"]["act_english"] = act_english.span.text
	else:
		data[college_name]["admissions"]["statistics"]["act_english"] = ''

	# act math
	act_math = act[2].find("div", {"class":"scalar__value"})
	if (act_math != None):
		data[college_name]["admissions"]["statistics"]["act_math"] = act_math.span.text
	else:
		data[college_name]["admissions"]["statistics"]["act_math"] = ''

	# act writing
	act_writing = act[3].find("div", {"class":"scalar__value"})
	if (act_writing != None):
		data[college_name]["admissions"]["statistics"]["act_writing"] = act_writing.span.text
	else:
		data[college_name]["admissions"]["statistics"]["act_writing"] = ''

	# act submission percentage
	act_submission_percentage = act[4].find("div", {"class":"scalar__value"})
	if (act_submission_percentage != None):
		data[college_name]["admissions"]["statistics"]["act_submission_percentage"] = act_submission_percentage.span.text
	else:
		data[college_name]["admissions"]["statistics"]["act_submission_percentage"] = ''


	# 'deadlines'
	data[college_name]["admissions"]["deadlines"] = {}
	deadlines = page_soup.find("section", {"id":"admissions-deadlines"}).find("div", {"class":"profile__buckets"})

	# bucket 1
	deadlines_1 = deadlines.find("div", {"class":"profile__bucket--1"}).div.div.findAll(recursive=False)
	
	# application deadline
	application_deadline = deadlines_1[0].find("div", {"class":"scalar__value"})
	if (application_deadline != None):
		data[college_name]["admissions"]["deadlines"]["application_deadline"] = application_deadline.span.text
	else:
		data[college_name]["admissions"]["deadlines"]["application_deadline"] = ''
	
	# early decision deadline
	early_decision_deadline = deadlines_1[1].find("div", {"class":"scalar__value"})
	if (early_decision_deadline != None):
		data[college_name]["admissions"]["deadlines"]["early_decision_deadline"] = early_decision_deadline.span.text
	else:
		data[college_name]["admissions"]["deadlines"]["early_decision_deadline"] = ''

	# early action deadline
	early_action_deadline = deadlines_1[2].find("div", {"class":"scalar__value"})
	if (early_action_deadline != None):
		data[college_name]["admissions"]["deadlines"]["early_action_deadline"] = early_action_deadline.span.text
	else:
		data[college_name]["admissions"]["deadlines"]["early_action_deadline"] = ''

	# offers early decision
	offers_early_decision = deadlines_1[3].find("div", {"class":"scalar__value"})
	if (offers_early_decision != None):
		data[college_name]["admissions"]["deadlines"]["offers_early_decision"] = offers_early_decision.span.text
	else:
		data[college_name]["admissions"]["deadlines"]["offers_early_decision"] = ''

	# offers early action
	offers_early_action = deadlines_1[4].find("div", {"class":"scalar__value"})
	if (offers_early_action != None):
		data[college_name]["admissions"]["deadlines"]["offers_early_action"] = offers_early_action.span.text
	else:
		data[college_name]["admissions"]["deadlines"]["offers_early_action"] = ''


	# bucket 2
	deadlines_2 = deadlines.find("div", {"class":"profile__bucket--2"}).div.div.findAll(recursive=False)

	# application fee
	application_fee = deadlines_2[0].find("div", {"class":"scalar__value"})
	if (application_fee != None):
		data[college_name]["admissions"]["deadlines"]["application_fee"] = application_fee.span.text
	else:
		data[college_name]["admissions"]["deadlines"]["application_fee"] = ''

	# application website
	application_website = deadlines_2[1].find("div", {"class":"profile__website__url"})
	if (application_website != None):
		data[college_name]["admissions"]["deadlines"]["application_website"] = application_website.text
	else:
		data[college_name]["admissions"]["deadlines"]["application_website"] = ''

	# accepts common app
	accepts_common_app = deadlines_2[2].find("div", {"class":"scalar__value"})
	if (accepts_common_app != None):
		data[college_name]["admissions"]["deadlines"]["accepts_common_app"] = accepts_common_app.span.text
	else:
		data[college_name]["admissions"]["deadlines"]["accepts_common_app"] = ''

	# accepts coalition app
	accepts_coalition_app = deadlines_2[3].find("div", {"class":"scalar__value"})
	if (accepts_coalition_app != None):
		data[college_name]["admissions"]["deadlines"]["accepts_coalition_app"] = accepts_coalition_app.span.text
	else:
		data[college_name]["admissions"]["deadlines"]["accepts_coalition_app"] = ''



	# 'requirements'
	data[college_name]["admissions"]["requirements"] = {}
	requirements = page_soup.find("section", {"id":"admissions-requirements"}).find("div", {"class":"profile__buckets"}).findAll("div", {"class":"fact__table__row__value"})

	data[college_name]["admissions"]["requirements"]["gpa"] = requirements[0].text
	data[college_name]["admissions"]["requirements"]["rank"] = requirements[1].text
	data[college_name]["admissions"]["requirements"]["transcript"] = requirements[2].text
	data[college_name]["admissions"]["requirements"]["college_prep_coures"] = requirements[3].text
	data[college_name]["admissions"]["requirements"]["sat/act"] = requirements[4].text
	data[college_name]["admissions"]["requirements"]["recommendations"] = requirements[5].text


	writeToJSONFile(path, fileName, data)