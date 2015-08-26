#!/usr/bin/env python
# -*- coding: iso-8859-15 -*-

htmlTemplate = '''
<!DOCTYPE>

<html>
<head>
    <title>Biodalliance Genome Browser</title>
    <script language="javascript" src="dalliance13.6a.js"></script>
    <script language="javascript">
      new Browser({
        //----------------------------------------------------------------------------------------------------
        fullscreen: true, // attempt to fit dalliance component to the containing window 
        maxHeight: 900,  // maximum hight in CSS pixels 
        pageName:     'mouseTwo-holder', // Target element ID
        //----------------------------------------------------------------------------------------------------
        chr:          '2', // Use the same name you have in your .2bit file
        viewStart: 132900815,
        viewEnd: 132915021,
    
        coordSystem: {
          speciesName: 'Mus musculus',
          taxon: 9606, // NCBI taxon if defined, set to zero if you dont't have one
          auth: 'Ensembl ', //Organization which did the gnoeme sequence/assemble
          version: '38',

        },
    
        sources:     [{name:        'Reference genome',
                       tier_type:   'Sequence',
                       desc:        'There will be longer desctiption placed here',
                       twoBitURI:   '%s'
                      },
                      {name:        'Annoatation',
                       desc:        'Genes annotation, showing Exons and Introns boundaries',
                       bwgURI:      '%s',
                       collapseSuperGroups: true,
                       trixURI:     '%s',
                      }, %s
                     ],
      });
    </script>
</head>
<body>
    <div id="mouseTwo-holder"></div>
</body>
</html>   
'''

bamTrackTemplate = '''
{name:      '%s',
                       disabled:     true, // This is "untick" track
                       bamURI:      '%s',
                       baiURI:      '%s.bai',
                       style: [{type: "density",
                                zoom: "low",

                                style: {glyph: "HISTOGRAM",
                                        COLOR1: "black",
                                        COLOR2: "red",
                                        HEIGHT: 30,
                                        }
                               },
                               {type: "density",
                                zoom: "medium",
                                style: {glyph: "HISTOGRAM",
                                        COLOR1: "black",
                                        COLOR2: "red",
                                        HEIGHT: 30,
                                        }
                               },
                               {type: "bam",
                                zoom: "high",
                                style: {glyph: "__SEQUENCE",
                                        FGCOLOR: "black",
                                        BGCOLOR: "blue",
                                        HEIGHT: 8,
                                        BUMP: true,
                                        LABEL: false,
                                        ZINDEX: 20,
                                        __SEQCOLOR: "mismatch"
                                       }
                               },

                              ],
                       },

'''
check = 'check'

import sys, os

refArg = sys.argv[1]
dataArg = sys.argv[2]

refFiles = os.listdir(refArg)
dataFiles = os.listdir(dataArg)

genome = ''
annotation = ''
index = ''

for i in refFiles:
    if i.endswith('.2bit'):
        genome = os.path.join(refArg, i)
    if i.endswith('bb'):
        annotation = os.path.join(refArg, i)
    if i.endswith('ix'):
        index = os.path.join(refArg, i)

bamTracks = []

for bamFile in dataFiles:
    if bamFile.endswith('sorted.bam'):
        name = bamFile.split('_')[0]
        bam = os.path.join(dataArg, bamFile)
        bamTrack = bamTrackTemplate % (name, bam, bam)
        bamTracks.append(bamTrack)

#print htmlTemplate % (genome, annotation, index, [i.strip() for i in bamTracks])
print htmlTemplate % (genome, annotation, index, ' '.join(bamTracks))
