import os
from turtle import down

import xml.etree.ElementTree as ElementTree

from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords

from rake_nltk import Rake

from datetime import date

bpmn_dir = 'models\\'
bpmn_files = os.listdir(bpmn_dir)

num = 1

# print('<div class="card-columns">')

for bpmn_file in bpmn_files:
    tree = ElementTree.parse(bpmn_dir + bpmn_file)
    root = tree.getroot()

    tasks = []

    for root_child in root:
        if 'process' in root_child.tag:
            process = root_child

            for process_child in process:
                if 'userTask' in process_child.tag:
                    task = process_child

                    tasks.append(task.get('name'))

    keywords = word_tokenize(' '.join(tasks))
    keywords = [word.lower() for word in keywords]
    keywords = [word for word in keywords if word.isalpha()]

    stop_words = set(stopwords.words('english'))
    keywords = [word for word in keywords if not word in stop_words]

    keywords = list(dict.fromkeys(keywords))

    rake = Rake(min_length=2)
    rake.extract_keywords_from_sentences(tasks)

    phrases = rake.get_ranked_phrases()

    file_name = ''.join([i.lower() for i in bpmn_file.replace(
        '.', ' ') if not i.isdigit()]).strip().replace(' ', '-') + '.html'

    model_name = bpmn_file.replace('.bpmn', '')
    model_name = ''.join([i for i in model_name.replace(
        '.', ' ') if not i.isdigit()]).strip()

    model_activities = ', '.join([''.join([i for i in task.replace(
        '.', ' ') if not i.isdigit()]).strip() for task in tasks])

    page_title = model_name + \
        ' — BPMN business process model based on the APQC PCF framework'
    page_description = ', '.join(phrases) + ' — ' + model_name
    page_keywords = ' '.join(keywords)

    product_id = 'APQCBPMN' + str(num)

    download_bpmn = 'https://raw.githubusercontent.com/freebpmnquality/apqc-pcf-bpmn-collection/main/models/' + bpmn_file

    page_url = 'https://freebpmnquality.github.io/business-models/' + file_name

    """
    print('''
    <div class="card">
        <div class="card-body">
            <h5 class="card-title">''' + model_name + '''</h5>
            <p class="card-text">''' + model_activities + '''</p>
            <p class="card-text"><small class="text-muted"><a href="business-models/''' + file_name + '''" target="_blank">View model</a></small></p>
        </div>
    </div>''')
    """

    """
    print('{ name: "' + model_name + '", activities: "' +
          model_activities + '", file: "' + file_name + '" },')
    """

    print('<url><loc>' + page_url + '</loc><changefreq>monthly</changefreq></url>')

    num += 1

    published_date = date.today().strftime('%Y-%m-%d')

    page_content = '''
<!DOCTYPE html>
<html lang="en">

<head>
    <!-- Global site tag (gtag.js) - Google Analytics -->
    <script async src="https://www.googletagmanager.com/gtag/js?id=G-W3TJ27QQ4T"></script>
    <script>
        window.dataLayer = window.dataLayer || [];

        function gtag() {
            dataLayer.push(arguments);
        }
        gtag('js', new Date());

        gtag('config', 'G-W3TJ27QQ4T');
    </script>

    <title>''' + page_title + '''</title>
    <meta name="title" content="''' + page_title + '''">
    <meta name="description" content="''' + page_description + '''">

    <meta property="og:type" content="website">
    <meta property="og:title" content="''' + page_title + '''">
    <meta property="og:description" content="''' + page_description + '''">

    <meta property="twitter:card" content="summary_large_image">
    <meta property="twitter:title" content="''' + page_title + '''">
    <meta property="twitter:description" content="''' + page_description + '''">

    <meta name="keywords" content="''' + page_keywords + '''">
    <meta name="robots" content="index, follow">
    <meta http-equiv="Content-Type" content="text/html; charset=utf-8">
    <meta name="language" content="English">

    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">

    <link rel="stylesheet" href="../css/bootstrap.min.css" />
    <link href="https://fonts.googleapis.com/css?family=Kanit" rel="stylesheet" />
    <link rel="stylesheet" href="../css/main.css" />
    <link rel="icon" type="image/png" href="../images/favicon.png" />

    <script async src="https://pagead2.googlesyndication.com/pagead/js/adsbygoogle.js?client=ca-pub-8990058470889069" crossorigin="anonymous"></script>

    <style>
        body {
            background: rgb(253, 197, 29);
            background: radial-gradient(circle, rgba(253, 197, 29, 0.2) 50%, rgba(252, 102, 69, 0.2) 100%);
        }

        .canvas {
            background-color: white;
            border-radius: 0.25rem;
            border: 1px solid rgba(0, 0, 0, .125);
        }

        #footer {
            background-color: transparent;
        }
    </style>
</head>

<body id="home">
    <nav class="navbar sticky-top navbar-expand-lg navbar-light bg-light">
        <a class="navbar-brand" href="javascript:void(0);" style="font-weight: bold;">freebpmnquality</a>
        <button class="navbar-toggler" type="button" data-toggle="collapse" data-target="#navbarNav" aria-controls="navbarNav" aria-expanded="false" aria-label="Toggle navigation">
            <span class="navbar-toggler-icon"></span>
        </button>
        <div class="collapse navbar-collapse" id="navbarNav">
            <ul class="navbar-nav">
                <li class="nav-item">
                    <a class="nav-link" href="/index.html">Home</a>
                </li>
                <li class="nav-item">
                    <a class="nav-link" href="/kbase.html">Knowledge Base</a>
                </li>
                <li class="nav-item">
                    <a class="nav-link" href="../apqc-bpmn.html">Get FREE BPMN Models of APQC PCF Cross Industry Process Classification Framework</a>
                </li>
            </ul>
        </div>
    </nav>

    <div itemscope itemtype="http://schema.org/Product" class="ml-4 mr-4 mt-4 mb-4">
        <small><a href="/kbase.html" class="text-muted">Knowledge Base</a> &gt;</small> <a href="/kbase.html#models" class="text-muted"><small itemprop="category">Models</small></a> &gt;</small> <a href="../apqc-bpmn.html" class="text-muted"><small itemprop="category">Get FREE BPMN Models of APQC PCF Cross Industry Process Classification Framework</small></a>
        <div class="row">
            <div class="col-sm-9 mt-2">
                <a href="''' + page_url + '''" itemprop="url">''' + page_title + '''</a>
                <br>

                <div class="canvas mt-2">
                    <div id="js-canvas"></div>
                </div>
                <br>

                <div itemprop="review" itemscope itemtype="http://schema.org/Review" class="mt-0">
                    <span itemprop="reviewRating" itemscope itemtype="http://schema.org/Rating">
                        <meta itemprop="worstRating" content="1">
                        <meta itemprop="bestRating" content="5">
                        <meta itemprop="ratingValue" content="5">
                    </span>

                    <h5 itemprop="itemReviewed">''' + page_title + '''</h5>

                    <span itemprop="author" itemscope itemtype="http://schema.org/Person">
                        <span itemprop="name" class="text-muted">freebpmnquality</span>
                    </span>
                    <br>

                    <small itemprop="reviewBody">The ''' + model_name + ''' BPMN model describes a business process that includes the following activities: ''' + model_activities + '''. This business process model is based on the APQC's PCF® framework. [<a href="https://www.apqc.org/process-frameworks" target="_blank">Source</a>]</small>
                    <br>
                    <small>Published on</small> <small itemprop="datePublished" class="text-muted">''' + published_date + '''</small>
                </div>
            </div>
            <div class="col-sm-3 mt-2">
                <h1 itemprop="name">''' + page_title + '''</h1>
                <h2 itemprop="brand">SCOR, BPMN</h2>

                <h6><span itemprop="productID" class="text-muted">''' + product_id + '''</span></h6>
                <meta itemprop="identifier_exists" content="no" />
                <meta itemprop="mpn" content="ANG" />
                <meta itemprop="sku" content="''' + product_id + '''" />

                <h6 itemprop="description">''' + page_description + '''</h6>

                <span itemprop="offers" itemscope itemtype="http://schema.org/Offer">
                    <link itemprop="availability" href="http://schema.org/InStock" />
                    <meta itemprop="priceCurrency" content="USD" />
                    <meta itemprop="priceValidUntil" content="2021-12-31" />
                    <meta itemprop="url" content="''' + page_url + '''" />
                    <h5 style="font-weight: bold;">$<span itemprop="price">0</span> <small></small> <span class="badge badge-danger">FREE</span></h5>
                </span>

                <a class="btn btn-outline-success mt-1" href="''' + download_bpmn + '''" role="button" target="_blank">Get BPMN</a>

                <div itemprop="aggregateRating" itemscope itemtype="http://schema.org/AggregateRating" class="mt-2">
                    <meta itemprop="bestRating" content="5" />
                    <meta itemprop="worstRating" content="1" />
                    <meta itemprop="ratingValue" content="5" />
                    <meta itemprop="ratingCount" content="1" />
                </div>

                <div class="card mt-4">
                    <a href="https://cloudfreebpmnquality.herokuapp.com/storage/index.html?collection=https://raw.githubusercontent.com/freebpmnquality/apqc-pcf-bpmn-collection/main/etherbpmn-collection/07649a3505baa4e4cf1d07b4809d0b59b42d32afcbe886c473d87de82675e421.etherbpmn"
                        target="_blank"><img src="https://cloudfreebpmnquality.herokuapp.com/storage/img/favicon.png" class="card-img-top" alt="calculator"></a>
                    <div class="card-body">
                        <h5 class="card-title"><a href="https://cloudfreebpmnquality.herokuapp.com/storage/index.html?collection=https://raw.githubusercontent.com/freebpmnquality/apqc-pcf-bpmn-collection/main/etherbpmn-collection/07649a3505baa4e4cf1d07b4809d0b59b42d32afcbe886c473d87de82675e421.etherbpmn"
                                target="_blank">Free Online Distributed Collection of BPMN Models</a></h5>
                        <p class="card-text">Free online software to exchange BPMN models in a distributed blockchain-driven collection. Disclaimer: it is a proof of concept that should be used with maximum discretion.</p>
                    </div>
                </div>
            </div>
        </div>
    </div>

    <div class="jumbotron text-muted" id="footer">
        <br>
        <a href="/index.html" class="btn btn-link" tabindex="-1" role="button" aria-disabled="true" style="font-weight: bold;">HOME</a>
        <a href="/kbase.html" class="btn btn-link" tabindex="-1" role="button" aria-disabled="true" style="font-weight: bold;">KNOWLEDGE BASE</a>
        <a href="../apqc-bpmn.html" class="btn btn-link">Get FREE BPMN Models of APQC PCF Cross Industry Process Classification Framework</a>
        <br>
        <br>
        <b>freebpmnquality</b> — Free Online BPMN Quality Analysis Service, 2020 -
        <script>
            document.write(new Date().getFullYear())
        </script> <a href="https://creativecommons.org/licenses/by-nd/4.0/" target="_blank">(CC BY-ND)</a>
    </div>

    <script src="../js/jquery-3.4.1.min.js"></script>
    <script src="../js/bootstrap.min.js"></script>
    <script src="../js/popper.min.js"></script>

    <script src="https://unpkg.com/bpmn-js@9.2.0/dist/bpmn-viewer.development.js"></script>

    <script>
        var viewer = new BpmnJS({
            container: $('#js-canvas'),
            height: 600
        });

        $(document).ready(function() {
            $.ajax(\'''' + download_bpmn + '''\', { dataType : 'text' }).done(async function(xml) {
                try {
                    await viewer.importXML(xml);
                    viewer.get('canvas').zoom('fit-viewport');
                } catch (err) {
                    console.error(err);
                }
            });
        });
    </script>
</body>

</html>'''

    with open('C:\\Users\\kopp9\\Documents\\GitHub\\freebpmnquality.github.io\\business-models\\' + file_name, 'w', encoding='utf-8') as file:
        file.write(page_content)

# print('</div>')
