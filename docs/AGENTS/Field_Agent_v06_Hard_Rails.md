---
project: Career Intelligence Space
type: spec
status: draft
tags: [field_agent, v06, hard_rails, frontmatter, assets, exif, privacy]
updated: 2025-09-30
---

# Field Agent v0.6 - Hard Rails Specification
**Status:** Draft - Hard Rails Implementation  
**Date:** 2025-09-30

## 🎯 Purpose

This document defines the hard rails for Field Agent v0.6, including the exact 4-key frontmatter schema, assets path conventions, EXIF scrubbing rules, and privacy protection measures. It addresses the operational pain points of YAML parsing errors and data privacy.

## 🔧 Hard Rails Frontmatter Schema

### **Exact 4 Keys (Nothing Else):**
```yaml
---
run_id: 2025-09-30T14:32-07:00
tag: Plumbing
loc: PDX-NE
status: draft
---
```

### **Field Definitions:**
- **run_id:** ISO timestamp with timezone (YYYY-MM-DDTHH:MM:SS-HH:MM)
- **tag:** One of 6 predefined tags (Plumbing, Electrical, Mounting, Smart-Home, Appliance, General)
- **loc:** Location code (PDX-NE, Seattle-Downtown, etc.)
- **status:** Always "draft" for new captures

### **Validation Rules:**
1. **Exactly 4 keys** - No more, no less
2. **No comments** - YAML comments not allowed
3. **No optional fields** - All fields required
4. **No nested objects** - Flat structure only
5. **No arrays** - Single values only

## 📁 Assets Path Convention

### **Directory Structure:**
```
/09_FIELD/YYYYMMDD_HHMM_{loc}_{tag}/
├── capture.md
└── assets/
    ├── IMG_0001.jpg
    ├── IMG_0002.jpg
    └── IMG_0003.jpg
```

### **Naming Convention:**
- **Folder:** `YYYYMMDD_HHMM_{location}_{tag}`
- **Assets:** `IMG_XXXX.jpg` (sequential numbering)
- **Capture file:** `capture.md`

### **Examples:**
```
/09_FIELD/20250930_1432_PDX-NE_Plumbing/
├── capture.md
└── assets/
    ├── IMG_0001.jpg
    ├── IMG_0002.jpg
    └── IMG_0003.jpg

/09_FIELD/20250930_0915_Seattle-Downtown_Electrical/
├── capture.md
└── assets/
    ├── IMG_0001.jpg
    └── IMG_0002.jpg
```

## 🖼️ Auto-Embed Pattern

### **Capture.md Body:**
```markdown
## Dump
- Voice note: transcript...
- Photo: [IMG_0001.jpg] (example placeholder)
- Quick note: "Toilet fill valve bypassed; recommend retrofit"

## Later-structure (agent can backfill)
- Parts: (blank)
- Time: (blank)
- Outcome: (blank)
```

### **Image Embedding:**
```markdown
[IMG_0001.jpg] (example placeholder)
[IMG_0002.jpg] (example placeholder)
[IMG_0003.jpg] (example placeholder)
```

## 🔒 EXIF/GPS Scrubbing Rules

### **Privacy Protection:**
1. **Strip EXIF data** - Remove all metadata from images
2. **Remove GPS coordinates** - No location data in images
3. **Remove timestamps** - No creation/modification dates
4. **Remove device info** - No camera/phone identification
5. **Remove personal data** - No user/owner information

### **Implementation:**
```python
def scrub_image_metadata(image_path):
    """
    Remove all EXIF and GPS data from image
    """
    from PIL import Image
    import os
    
    # Open image
    image = Image.open(image_path)
    
    # Remove EXIF data
    data = list(image.getdata())
    image_without_exif = Image.new(image.mode, image.size)
    image_without_exif.putdata(data)
    
    # Save without metadata
    image_without_exif.save(image_path, quality=85, optimize=True)
    
    return image_path
```

### **File Size Limits:**
- **Maximum size:** 5MB per image
- **Maximum count:** 10 images per capture
- **Format:** JPEG only
- **Compression:** 85% quality, optimized

## 🚨 Privacy Protection Rules

### **Filename Restrictions:**
- **No tenant names** - Never include client/tenant names in filenames
- **No addresses** - Never include street addresses in filenames
- **No personal info** - Never include personal information in filenames
- **Location codes only** - Use generic location codes (PDX-NE, Seattle-Downtown)

### **Body Content Rules:**
- **Sensitive details in body only** - Client names, addresses, personal info in body text
- **No sensitive data in frontmatter** - Keep frontmatter generic
- **PII scanning** - Automatic PII detection and flagging
- **Manual review** - Sensitive captures require manual review

### **Examples:**
```yaml
# ✅ GOOD - Generic location code
loc: PDX-NE

# ❌ BAD - Specific address
loc: 123-Main-St-Portland

# ✅ GOOD - Generic tag
tag: Plumbing

# ❌ BAD - Client-specific tag
tag: Smith-Family-Plumbing
```

## 🔧 Frontmatter Validation

### **Hard Rails Linter:**
```python
def validate_frontmatter(frontmatter):
    """
    Validate frontmatter against hard rails schema
    """
    required_keys = ["run_id", "tag", "loc", "status"]
    
    # Check exact key count
    if len(frontmatter) != 4:
        raise ValueError(f"Frontmatter must have exactly 4 keys, got {len(frontmatter)}")
    
    # Check required keys
    for key in required_keys:
        if key not in frontmatter:
            raise ValueError(f"Missing required key: {key}")
    
    # Check for extra keys
    for key in frontmatter:
        if key not in required_keys:
            raise ValueError(f"Extra key not allowed: {key}")
    
    # Validate run_id format
    import re
    run_id_pattern = r'^\d{4}-\d{2}-\d{2}T\d{2}:\d{2}:\d{2}-\d{2}:\d{2}$'
    if not re.match(run_id_pattern, frontmatter["run_id"]):
        raise ValueError(f"Invalid run_id format: {frontmatter['run_id']}")
    
    # Validate tag
    valid_tags = ["Plumbing", "Electrical", "Mounting", "Smart-Home", "Appliance", "General"]
    if frontmatter["tag"] not in valid_tags:
        raise ValueError(f"Invalid tag: {frontmatter['tag']}. Must be one of: {valid_tags}")
    
    # Validate status
    if frontmatter["status"] != "draft":
        raise ValueError(f"Status must be 'draft', got: {frontmatter['status']}")
    
    return True
```

### **Error Messages:**
```
❌ Frontmatter validation failed: Extra key not allowed: 'notes'
   • Allowed keys: run_id, tag, loc, status
   • Remove extra keys and try again

❌ Frontmatter validation failed: Invalid tag: 'HVAC'
   • Valid tags: Plumbing, Electrical, Mounting, Smart-Home, Appliance, General
   • Use one of the valid tags

❌ Frontmatter validation failed: Invalid run_id format: '2025-09-30 14:32'
   • Required format: YYYY-MM-DDTHH:MM:SS-HH:MM
   • Example: 2025-09-30T14:32:00-07:00
```

## 📊 File Generation Logic

### **Capture File Creation:**
```python
def create_capture_file(issue_data, folder_path):
    """
    Create capture.md file with hard rails frontmatter
    """
    # Generate frontmatter
    frontmatter = {
        "run_id": generate_run_id(),
        "tag": issue_data.tag,
        "loc": issue_data.location,
        "status": "draft"
    }
    
    # Validate frontmatter
    validate_frontmatter(frontmatter)
    
    # Generate body
    body = f"""# Field Capture - {issue_data.tag}

## Dump
- Photos: {len(issue_data.attachments)} attached
- Note: {issue_data.note}
- Location: {issue_data.location}
- Time: {issue_data.timestamp}

## Later-structure (agent can backfill)
- Parts: (blank)
- Time: (blank)
- Outcome: (blank)
- Client: (blank)
"""
    
    # Add image embeds (example - actual implementation will save real images)
    for i, attachment in enumerate(issue_data.attachments, 1):
        body += f"\n[IMG_{i:04d}.jpg] (will be saved to assets/)\n"
    
    # Write file
    capture_path = os.path.join(folder_path, "capture.md")
    with open(capture_path, 'w') as f:
        f.write("---\n")
        f.write(yaml.dump(frontmatter, default_flow_style=False))
        f.write("---\n\n")
        f.write(body)
    
    return capture_path
```

## 🔧 Asset Processing

### **Image Processing Pipeline:**
```python
def process_attachments(attachments, assets_path):
    """
    Process and store image attachments
    """
    processed_images = []
    
    for i, attachment in enumerate(attachments, 1):
        # Generate filename
        filename = f"IMG_{i:04d}.jpg"
        file_path = os.path.join(assets_path, filename)
        
        # Download and save
        download_attachment(attachment, file_path)
        
        # Scrub metadata
        scrub_image_metadata(file_path)
        
        # Validate file size
        if os.path.getsize(file_path) > 5 * 1024 * 1024:  # 5MB
            raise ValueError(f"Image too large: {filename}")
        
        processed_images.append(filename)
    
    return processed_images
```

## 🚨 Error Handling

### **Frontmatter Errors:**
```
❌ Frontmatter validation failed: Missing required key: 'tag'
   • Required keys: run_id, tag, loc, status
   • Add missing key and try again

❌ Frontmatter validation failed: Invalid run_id format: '2025-09-30'
   • Required format: YYYY-MM-DDTHH:MM:SS-HH:MM
   • Example: 2025-09-30T14:32:00-07:00
```

### **Asset Errors:**
```
❌ Image processing failed: Image too large: IMG_0001.jpg
   • Maximum size: 5MB
   • Current size: 8.2MB
   • Compress image and try again

❌ Asset processing failed: Invalid file format: IMG_0001.png
   • Supported formats: JPEG only
   • Convert to JPEG and try again
```

### **Privacy Errors:**
```
⚠️ Privacy warning: Filename contains sensitive data
   • Filename: 123-Main-St-Plumbing.jpg
   • Use generic location codes only
   • Rename file and try again

⚠️ PII detected in content: Client name found
   • Content: "Smith family plumbing issue"
   • Move sensitive data to body text only
   • Review and resubmit
```

## 📱 Mobile Considerations

### **Image Capture:**
- **Size limits** - Warn user about 5MB limit
- **Format conversion** - Auto-convert to JPEG if needed
- **Metadata stripping** - Automatic EXIF removal
- **Compression** - Auto-compress large images

### **Form Validation:**
- **Real-time validation** - Check frontmatter as user types
- **Error prevention** - Disable submit until valid
- **Help text** - Show examples and requirements
- **Auto-complete** - Suggest valid tags and locations

---

## 🎯 Key Takeaways

1. **Hard rails prevent errors** - Exact 4-key schema with no flexibility
2. **Privacy by design** - Automatic EXIF scrubbing and PII protection
3. **Consistent structure** - Standardized paths and naming conventions
4. **Clear validation** - Precise error messages and recovery steps
5. **Mobile optimized** - Size limits and format handling

---

*Field Agent v0.6 Hard Rails Specification - Career Intelligence Space*
*Status: Draft - Hard Rails Implementation*
